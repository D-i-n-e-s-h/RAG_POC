import os

from document_loader import DocumentLoader
from services.embedding_service import EmbeddingService
from services.faiss_service import FaissService
from services.bm25_service import BM25Service
from services.hybrid_search import HybridSearch

DOCUMENT_FOLDER = "documents"
MODEL_NAME = "nomic-embed-text"
TOP_K = 3


def main():

    faiss_service = FaissService()
    bm25_service = BM25Service()
    embedding_service = EmbeddingService(MODEL_NAME)

    # -----------------------------
    # Create index (First Run)
    # -----------------------------
    if not os.path.exists("embeddings/faiss.index"):

        print("Creating new FAISS index...")

        loader = DocumentLoader(DOCUMENT_FOLDER)

        documents = loader.load_documents()

        embeddings = embedding_service.generate_embeddings(documents)

        embeddings = faiss_service.normalize(embeddings)

        faiss_service.build_index(embeddings)

        faiss_service.save_embeddings(embeddings)
        faiss_service.save_metadata(documents)
        faiss_service.save_index()

        print("Index created successfully.\n")

    # -----------------------------
    # Load Existing Index
    # -----------------------------
    else:

        print("Loading existing FAISS index...\n")

        documents = faiss_service.load_metadata()

        embeddings = faiss_service.load_embeddings()

        faiss_service.load_index()

    # -----------------------------
    # Build BM25 Index
    # -----------------------------
    bm25_service.build_index(documents)

    # -----------------------------
    # Search Loop
    # -----------------------------
    while True:

        query = input("\nAsk a question ('exit' to quit): ")

        if query.lower() == "exit":
            break

        # -------------------------
        # FAISS Search
        # -------------------------
        query_embedding = embedding_service.generate_query_embedding(query)

        faiss_scores, faiss_indexes = faiss_service.search(
            query_embedding,
            TOP_K
        )

        # -------------------------
        # BM25 Search
        # -------------------------
        bm25_results  = bm25_service.search(query, TOP_K)
        
        results = HybridSearch.search(
            faiss_scores,
            faiss_indexes,
            bm25_results,
            TOP_K
        )
        
        print("\n========== HYBRID SEARCH ==========\n")

        for index, hybrid, faiss_score, bm25_score in results:

            print(f"File : {documents[index]['file_name']}")
            print(f"Hybrid Score : {hybrid:.3f}")
            print(f"Semantic Score : {faiss_score:.3f}")
            print(f"BM25 Score : {bm25_score:.3f}")
            print(documents[index]["content"])
            print("-"*60)



if __name__ == "__main__":
    main()