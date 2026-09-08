"""
Agent Loop

Supports multiple tool calls until the LLM
decides it has enough information.
"""

from llm.llm_service import LLMService
from llm.tool_registry import ToolRegistry
from llm.tool_executor import ToolExecutor
import json

class AgentLoop:

    MAX_ITERATIONS = 10

    def __init__(self):

        self.llm = LLMService()

        self.registry = ToolRegistry()

        self.executor = ToolExecutor()

    def run(self, user_message: str):

        messages = [
            {
                "role": "system",
                "content": """
                You are a helpful AI assistant.

                You have access to external tools.

                Rules:

                1. Use a tool only if it is required to answer the user's request.
                2. If no tool is required, answer the user naturally.
                3. Never mention:
                - tools
                - function calls
                - tool execution
                - whether a tool was used
                4. The user should never know whether a tool was invoked.
                5. Return only the final assistant response.
                """
            },
            {
                "role": "user",
                "content": user_message
            }
        ]

        tools = self.registry.get_tool_schemas()

        iteration = 0

        while iteration < self.MAX_ITERATIONS:

            iteration += 1

            response = self.llm.chat(
                messages=messages,
                tools=tools
            )
            # print("\n========== FIRST LLM RESPONSE ==========")
            # print(response)

            assistant_message = response.message

            # print("\nAssistant Message:")
            # print(assistant_message)

            # print("\nTool Calls:")
            # print(assistant_message.tool_calls)

            # Save assistant response
            messages.append(assistant_message)

            # No tool call means final answer
            if not assistant_message.tool_calls:

                return assistant_message.content

            # Execute every requested tool
            for tool_call in assistant_message.tool_calls:

                tool_name = tool_call.function.name

                arguments = tool_call.function.arguments

                tool_result = self.executor.execute(
                    tool_name,
                    arguments
                )

                messages.append({
                    "role": "tool",
                    "name": tool_name,
                    "content": json.dumps(tool_result)
                })

        return "Maximum agent iterations reached."