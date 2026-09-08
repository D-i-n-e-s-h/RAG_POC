class HybridSearch:

    @staticmethod
    def normalize(scores):

        max_score = max(scores)

        if max_score == 0:
            return scores

        return [
            score / max_score
            for score in scores
        ]

    @staticmethod
    def search(
        faiss_scores,
        faiss_indexes,
        bm25_results,
        top_k
    ):

        bm25_scores = [score for _, score in bm25_results]

        normalized = HybridSearch.normalize(
            bm25_scores
        )

        merged = {}

        # FAISS scores
        for score, index in zip(
            faiss_scores[0],
            faiss_indexes[0]
        ):

            merged[index] = {
                "faiss": float(score),
                "bm25": 0
            }

        # BM25 scores
        for (index, _), score in zip(
            bm25_results,
            normalized
        ):

            if index not in merged:

                merged[index] = {
                    "faiss": 0,
                    "bm25": score
                }

            else:

                merged[index]["bm25"] = score

        results = []

        for index, values in merged.items():

            hybrid = (
                values["faiss"] * 0.5
                +
                values["bm25"] * 0.5
            )

            results.append(
                (
                    index,
                    hybrid,
                    values["faiss"],
                    values["bm25"]
                )
            )

        results.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return results[:top_k]