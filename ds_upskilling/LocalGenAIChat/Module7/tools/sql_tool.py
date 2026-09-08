"""
SQL Tool

Mock implementation for Module 7.
Later we'll replace this with Text-to-SQL + SQLite.
"""


class SQLTool:

    @property
    def name(self):
        return "execute_sql"

    @property
    def description(self):
        return "Use this tool ONLY when the user asks about company employees, sales, customers, orders, products, or any information stored in the company's internal database."

    @property
    def parameters(self):
        return {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "Natural language database question."
                }
            },
            "required": ["question"]
        }

    def execute(self, arguments):

        question = arguments.get("question")

        # Mock response
        return {
            "question": question,
            "rows": [
                {
                    "month": "January",
                    "average_sales": 25000
                },
                {
                    "month": "February",
                    "average_sales": 32000
                }
            ]
        }