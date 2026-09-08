from config import VECTOR_DB

from services import faiss_service

# Chroma will be imported later


def add_documents(chunks, embeddings):

    if VECTOR_DB == "faiss":
        return faiss_service.add_documents(
            chunks,
            embeddings
        )

    raise Exception("Unsupported Vector DB")


def search(query_embedding, top_k=5):

    if VECTOR_DB == "faiss":
        return faiss_service.search(
            query_embedding,
            top_k
        )

    raise Exception("Unsupported Vector DB")