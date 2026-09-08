from ddgs import DDGS


class WebSearchTool:

    @property
    def name(self):
        return "web_search"

    @property
    def description(self):
        return "Search the web."

    @property
    def parameters(self):
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query."
                }
            },
            "required": ["query"]
        }

    def execute(self, arguments):

        query = arguments.get("query")

        try:

            results = []

            with DDGS() as ddgs:

                for item in ddgs.text(
                    query,
                    max_results=5
                ):

                    results.append({

                        "title": item["title"],

                        "url": item["href"],

                        "snippet": item["body"]
                    })

            return {

                "success": True,

                "query": query,

                "results": results
            }

        except Exception as ex:

            return {

                "success": False,

                "error": str(ex)
            }