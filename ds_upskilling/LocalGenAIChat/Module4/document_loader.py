from pathlib import Path


class DocumentLoader:

    def __init__(self, document_folder):
        self.document_folder = Path(document_folder)

    def load_documents(self):

        documents = []

        for file in self.document_folder.glob("*.txt"):

            text = file.read_text(encoding="utf-8")

            documents.append(
                {
                    "file_name": file.name,
                    "content": text
                }
            )

        return documents