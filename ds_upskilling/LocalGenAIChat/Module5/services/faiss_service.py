import faiss
import numpy as np
import json
import os

class FaissService:

    def __init__(self):
        self.index = None

    def build_index(self, embeddings):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(embeddings)

        print(f"Indexed {self.index.ntotal} documents")

    def normalize(self, embeddings):

        faiss.normalize_L2(embeddings)

        return embeddings

    def search(self, query_embedding, top_k):

        faiss.normalize_L2(query_embedding)

        scores, indexes = self.index.search(query_embedding, top_k)

        return scores, indexes

    def save_embeddings(self, embeddings):

        os.makedirs("embeddings", exist_ok=True)

        np.save(
            "embeddings/embeddings.npy",
            embeddings
        )
        
    def load_embeddings(self):

        return np.load(
            "embeddings/embeddings.npy"
        )
    
    def save_metadata(self, documents):

        os.makedirs("embeddings", exist_ok=True)

        with open(
            "embeddings/metadata.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                documents,
                file,
                indent=4
            )
            
    def load_metadata(self):

        with open(
            "embeddings/metadata.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)
        
    def save_index(self):

        os.makedirs("embeddings", exist_ok=True)

        faiss.write_index(
            self.index,
            "embeddings/faiss.index"
        )
        
    def load_index(self):

        if not os.path.exists("embeddings/faiss.index"):
            raise FileNotFoundError(
                "FAISS index not found."
            )

        self.index = faiss.read_index(
            "embeddings/faiss.index"
        )