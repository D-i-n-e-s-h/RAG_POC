"""
Tool Executor

Responsible for executing tools selected by the LLM.

It receives

Tool Name
Arguments

↓

Finds matching tool

↓

Executes it

↓

Returns result
"""


from llm.tool_registry import ToolRegistry


class ToolExecutor:

    def __init__(self):

        registry = ToolRegistry()

        self.tools = registry.get_tool_instances()

    def execute(self, tool_name: str, arguments: dict):

        tool = self.tools.get(tool_name)

        if tool is None:
            raise Exception(f"Unknown tool: {tool_name}")

        return tool.execute(arguments)