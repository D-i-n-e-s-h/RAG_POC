import chromadb
import uuid


class ChromaService:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="chroma_db")

        self.collection = self.client.get_or_create_collection(name="knowledge_base")

    def add_documents(self, documents, embeddings):

        ids = []
        texts = []
        metadatas = []

        for document in documents:

            ids.append(str(uuid.uuid4()))

            texts.append(document["content"])

            metadatas.append(
                {"file_name": document["file_name"], "source": document["file_name"]}
            )

        self.collection.add(
            ids=ids,
            documents=texts,
            embeddings=embeddings.tolist(),
            metadatas=metadatas,
        )

        print(f"Indexed {len(documents)} documents into Chroma.")

    def count(self):
        return self.collection.count()

    def search(self, query_embedding, top_k=5):

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k,
            include=["documents", "metadatas", "distances"],
        )
        # documents = []
        # for i in range(len(results["documents"][0])):

        #     distance = results["distances"][0][i]

        #     if distance < 0.4:

        #         documents.append({
        #             "content": results["documents"][0][i],
        #             "distance": distance,
        #             "metadata": results["metadatas"][0][i]
        #         })

        # return documents
        return results
    
    def search_by_file(
        self,
        query_embedding,
        file_name,
        top_k=5
    ):

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k,
            where={
                "file_name": file_name
            },
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        return results
