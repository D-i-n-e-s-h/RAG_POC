"""
LLM Service

Responsible for communicating with Ollama.

Responsibilities
----------------
- Send messages
- Send tool schemas
- Return raw response

It DOES NOT

- Execute tools
- Parse tool calls
- Maintain memory
"""

from ollama import chat
import config


class LLMService:

    def __init__(self):

        self.model = config.MODEL

    def chat(self, messages, tools=None):

        request = {
            "model": self.model,
            "messages": messages
        }

        if tools:
            request["tools"] = tools

        response = chat(**request)

        return response