from ollama import embed
import numpy as np


class EmbeddingService:

    def __init__(self, model):
        self.model = model

    def generate_embeddings(self, documents):

        texts = [
            document["content"]
            for document in documents
        ]

        response = embed(
            model=self.model,
            input=texts
        )

        embeddings = np.array(
            response["embeddings"],
            dtype=np.float32
        )

        return embeddings
    
    def generate_query_embedding(self, query):

        response = embed(
            model=self.model,
            input=query
        )

        return np.array(
            response["embeddings"],
            dtype=np.float32
        )