from config import THRESHOLD

class RetrievalService:

    def filter_results(
        results,
        threshold=THRESHOLD
    ):

        filtered = []

        for document, metadata, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        ):

            #print(str(distance) + "  " + metadata.get("file_name") + "  " + metadata.get("source"))
            #print("---------------")
            if distance <= threshold:

                filtered.append(
                    {
                        "content": document,
                        "file_name": metadata.get("file_name"),
                        "source": metadata.get("source"),
                        "distance": distance
                    }
                )
        return filtered