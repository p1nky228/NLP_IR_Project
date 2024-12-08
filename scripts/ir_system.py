import faiss
import numpy as np

def build_faiss_index(embeddings):
    """
    Создание индекса FAISS.

    :param embeddings: Список векторов
    :return: FAISS Index
    """
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))
    return index

def search(query_embedding, index, top_k=5):
    """
    Поиск ближайших соседей.

    :param query_embedding: Вектор запроса
    :param index: FAISS Index
    :param top_k: Количество результатов
    :return: Индексы ближайших соседей
    """
    distances, indices = index.search(query_embedding, top_k)
    return indices, distances

if __name__ == "__main__":
    dummy_embeddings = np.random.rand(10, 384).astype("float32")
    index = build_faiss_index(dummy_embeddings)

    query_embedding = np.random.rand(1, 384).astype("float32")
    results = search(query_embedding, index)
    print("Результаты поиска:", results)