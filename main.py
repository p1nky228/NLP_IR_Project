from scripts.parse_docx import parse_docx
from scripts.vectorize_data import vectorize_data
from scripts.ir_system import build_faiss_index, search
from scripts.evaluate import calculate_rouge, calculate_bertscore
from scripts.visualize_metrics import plot_metrics
from sentence_transformers import SentenceTransformer
import numpy as np
import json
import os

def run_pipeline(docx_path, model_name="all-MiniLM-L6-v2"):
    """
    Запуск полного пайплайна: парсинг, векторизация, поиск, оценка.

    :param docx_path: Путь к docx-файлу
    :param model_name: Название модели для векторизации
    """
    # 1. Парсинг данных
    print("Парсинг docx-файла...")
    parsed_data = parse_docx(docx_path)
    json_path = "data/parsed_data.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(parsed_data, f, ensure_ascii=False, indent=4)

    # 2. Векторизация данных
    print("Векторизация данных...")
    embeddings = vectorize_data(json_path, model_name=model_name)

    # 3. Построение FAISS-индекса
    print("Построение индекса...")
    index = build_faiss_index(embeddings)

    # 4. Поиск (пример запроса)
    print("Поиск по индексу...")
    model = SentenceTransformer(model_name)
    query = "Пример запроса из таблицы"
    query_embedding = model.encode([query])
    indices, distances = search(query_embedding, index)
    print("Результаты поиска:", indices)

    # 5. Оценка (пример)
    print("Оценка метрик...")
    reference = ["Пример эталонного ответа."]
    candidate = ["Пример сгенерированного ответа."]
    rouge_scores = calculate_rouge(reference, candidate)
    bert_scores = calculate_bertscore(reference, candidate)
    
    print("ROUGE:", rouge_scores)
    print("BERTScore:", bert_scores)

    # 6. Визуализация метрик
    print("Визуализация метрик...")
    metrics = {
        "Precision": [bert_scores["precision"]],
        "Recall": [bert_scores["recall"]],
        "F1": [bert_scores["f1"]]
    }
    # metrics = {
    # "Precision": [0.842, 0.85, 0.86],
    # "Recall": [0.887, 0.89, 0.9],
    # "F1": [0.864, 0.865, 0.87]
    # }

    plot_metrics(metrics, "BERTScore")


if __name__ == "__main__":
    # Убедимся, что примеры данных существуют
    if not os.path.exists("data/hard.docx"):
        from scripts.create_docx import create_hard_docx
        create_hard_docx("data/hard.docx")

    # Запуск пайплайна
    run_pipeline("data/hard.docx")
