import requests
from bs4 import BeautifulSoup


class BrowserTool:

    @property
    def name(self):
        return "browse_url"

    @property
    def description(self):
        return "Download a webpage and return its readable text."

    @property
    def parameters(self):
        return {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "URL to browse."
                }
            },
            "required": ["url"]
        }

    def execute(self, arguments):

        url = arguments.get("url")

        try:

            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            # Remove unnecessary tags
            for tag in soup([
                "script",
                "style",
                "noscript"
            ]):
                tag.decompose()

            title = ""

            if soup.title:
                title = soup.title.text.strip()

            paragraphs = []

            for p in soup.find_all("p"):

                text = p.get_text(
                    separator=" ",
                    strip=True
                )

                if text:
                    paragraphs.append(text)

            content = "\n".join(paragraphs[:20])

            return {

                "success": True,

                "url": url,

                "title": title,

                "content": content
            }

        except Exception as ex:

            return {

                "success": False,

                "error": str(ex)
            }