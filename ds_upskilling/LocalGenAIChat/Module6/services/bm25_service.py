from rank_bm25 import BM25Okapi


class BM25Service:

    def __init__(self):
        self.bm25 = None
        self.documents = None

    def build_index(self, documents):

        self.documents = documents

        tokenized_documents = [
            document["content"].lower().split()
            for document in documents
        ]

        self.bm25 = BM25Okapi(tokenized_documents)

        print(f"BM25 indexed {len(documents)} documents")
        
    def search(self, query, top_k):

        query_tokens = query.lower().split()

        scores = self.bm25.get_scores(query_tokens)

        ranked = sorted(
            enumerate(scores),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]