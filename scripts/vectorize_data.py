from sentence_transformers import SentenceTransformer
import json

def vectorize_data(json_file, model_name="all-MiniLM-L6-v2"):
    """
    Векторизация данных из JSON файла.

    :param json_file: Путь к JSON файлу с данными
    :param model_name: Название модели для векторизации
    :return: Список векторов
    """
    model = SentenceTransformer(model_name)
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    text_data = []
    for table in data["tables"]:
        text_data.extend([" ".join(row) for row in table])
    text_data.extend(data["lists"])

    embeddings = model.encode(text_data, show_progress_bar=True)
    return embeddings

if __name__ == "__main__":
    embeddings = vectorize_data("data/parsed_data.json")
    print("Данные успешно векторизованы.")