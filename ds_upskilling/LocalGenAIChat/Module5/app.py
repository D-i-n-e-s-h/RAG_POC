import os

from services.retrieval_service import RetrievalService
from services.memory_service import MemoryService
from services.document_loader import DocumentLoader
from services.embedding_service import EmbeddingService
from services.faiss_service import FaissService
from services.bm25_service import BM25Service
from services.hybrid_search import HybridSearch
from services.chroma_service import ChromaService
from services.prompt_builder import PromptBuilder
from services.llm_service import LLMService
from services.chunk_service import ChunkService
from config import DOCUMENT_FOLDER, LLM_MODEL, MAX_MESSAGES, MODEL_NAME, TOP_K


def main():

    faiss_service = FaissService()
    bm25_service = BM25Service()
    chroma_service = ChromaService()
    embedding_service = EmbeddingService(MODEL_NAME)
    llm_service = LLMService(LLM_MODEL)
    memory_service = MemoryService(MAX_MESSAGES)
    chunk_service = ChunkService(chunk_size=1000,overlap=200)
    
    loader = DocumentLoader(DOCUMENT_FOLDER)

    # -----------------------------
    # Create index (First Run)
    # -----------------------------
    if not os.path.exists("embeddings/faiss.index"):

        print("Creating new FAISS index...")

        # without chunking
        # documents = loader.load_documents()

        # embeddings = embedding_service.generate_embeddings(documents)

        # # Save into Chroma BEFORE normalization
        # chroma_service.add_documents(
        #     documents,
        #     embeddings
        # )
        
        # with chunking
        documents = loader.load_documents()

        chunks = chunk_service.chunk_documents(
            documents
        )

        embeddings = embedding_service.generate_embeddings(
            chunks
        )
        # Save into Chroma BEFORE normalization
        chroma_service.add_documents(
            chunks,
            embeddings
        )
        
        print(f"Documents Loaded : {len(documents)}")
        print(f"Chunks Created   : {len(chunks)}")
        print(f"Chroma Collection Count: {chroma_service.count()}")

        # FAISS still needs normalized vectors
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

        print("Loading existing Chroma and FAISS index...\n")

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
        
        # Chrom search
        results = chroma_service.search(
            query_embedding[0],
            top_k=3
        )

        chroma_result(results)
        
        filtered_results = RetrievalService.filter_results(
            results
        ) 

        prompt = PromptBuilder.build(
            query,
            filtered_results,
            memory_service.get_history()
        )
        
        memory_service.add_user_message(query)
        
        answer = llm_service.generate(prompt)
        
        memory_service.add_assistant_message(answer)
        
        print(answer)
        
        # faiss_scores, faiss_indexes = faiss_service.search(
        #     query_embedding,
        #     TOP_K
        # )

        # # -------------------------
        # # BM25 Search
        # # -------------------------
        # bm25_results  = bm25_service.search(query, TOP_K)
        
        # results = HybridSearch.search(
        #     faiss_scores,
        #     faiss_indexes,
        #     bm25_results,
        #     TOP_K
        # )
        
        # print("\n========== FAISS HYBRID SEARCH ==========\n")

        # for index, hybrid, faiss_score, bm25_score in results:

        #     print(f"File : {documents[index]['file_name']}")
        #     print(f"Hybrid Score : {hybrid:.3f}")
        #     print(f"Semantic Score : {faiss_score:.3f}")
        #     print(f"BM25 Score : {bm25_score:.3f}")
        #     print(documents[index]["content"])
        #     print("-"*60)



def chroma_result(chroma_results):
    print("\n========== CHROMA SEARCH ==========\n")
    for i in range(len(chroma_results["documents"][0])):

        print("=" * 60)

        print(
            f"Rank : {i+1}"
        )

        print(
            f"Distance : {chroma_results['distances'][0][i]}"
        )

        print(
            f"File : {chroma_results['metadatas'][0][i]['file_name']}"
        )

        print(
            f"Content :\n{chroma_results['documents'][0][i]}"
        )

        print()

if __name__ == "__main__":
    main()