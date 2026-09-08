import re

class ChunkService:

    def __init__(
        self,
        chunk_size=1000,
        overlap=200
    ):

        self.chunk_size = chunk_size
        self.overlap = overlap

        self.separators = [
            "\n\n",   # Paragraph
            "\n",     # Line
            ". ",     # Sentence
            " "       # Word
        ]

    def chunk_documents(self, documents):

        chunks = []

        for document in documents:

            texts = self.recursive_split(
                document["content"],
                self.separators
            )

            for index, text in enumerate(texts):

                chunks.append(
                    {
                        "file_name": document["file_name"],
                        "chunk_id": index + 1,
                        "content": text
                    }
                )

        return chunks

    def recursive_split(
        self,
        text,
        separators
    ):

        # Base case
        if len(text) <= self.chunk_size:
            return [text]

        # No separators left
        if not separators:
            return [
                text[i:i+self.chunk_size]
                for i in range(0, len(text), self.chunk_size)
            ]

        separator = separators[0]

        parts = text.split(separator)

        # If this separator couldn't split the text,
        # try the next separator.
        if len(parts) == 1:

            return self.recursive_split(
                text,
                separators[1:]
            )

        chunks = []

        for part in parts:

            if len(part) <= self.chunk_size:

                chunks.append(part)

            else:

                chunks.extend(
                    self.recursive_split(
                        part,
                        separators[1:]
                    )
                )

        return self.merge_chunks(
            chunks,
            separator
        )
        
    def merge_chunks(
        self,
        parts,
        separator
    ):

        chunks = []

        current_chunk = ""

        for part in parts:

            if not part.strip():
                continue

            if not current_chunk:

                current_chunk = part

                continue

            candidate = current_chunk + separator + part

            if len(candidate) <= self.chunk_size:

                current_chunk = candidate

            else:

                chunks.append(current_chunk)

                current_chunk = part

        if current_chunk:

            chunks.append(current_chunk)

        return chunks