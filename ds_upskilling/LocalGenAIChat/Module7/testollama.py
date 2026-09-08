from ollama import chat

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

response = chat(
    model="llama3.1:8b",
    messages=[
        {
            "role": "user",
            "content": "What is the weather in Singapore?"
        }
    ],
    tools=tools
)

print(response)