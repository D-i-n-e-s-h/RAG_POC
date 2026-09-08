from ollama import chat as ollama_chat
from config import MODEL

def chat(messages):
    response = ollama_chat(
        model=MODEL,
        messages=messages
    )

    return response["message"]["content"]