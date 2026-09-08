class DeduplicationService:

    @staticmethod
    def deduplicate(chunks):

        unique_chunks = []
        seen = set()

        for chunk in chunks:

            content = chunk["content"].strip()

            if content not in seen:

                seen.add(content)
                unique_chunks.append(chunk)

        return unique_chunks