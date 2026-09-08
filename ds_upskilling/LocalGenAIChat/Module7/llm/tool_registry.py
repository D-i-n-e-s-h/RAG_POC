"""
Tool Registry

Single source of truth for all tools.

Responsible for:
1. Registering tools
2. Providing tool schemas to LLM
3. Providing tool instances to ToolExecutor
"""

from tools.weather_tool import WeatherTool
from tools.sql_tool import SQLTool
from tools.web_search_tool import WebSearchTool
from tools.browser_tool import BrowserTool


class ToolRegistry:

    def __init__(self):

        self.tools = [
            WeatherTool(),
            SQLTool(),
            WebSearchTool(),
            BrowserTool()
        ]

    def get_tool_schemas(self):

        schemas = []

        for tool in self.tools:

            schemas.append(
                {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.parameters
                    }
                }
            )

        return schemas

    def get_tool_instances(self):

        return {
            tool.name: tool
            for tool in self.tools
        }