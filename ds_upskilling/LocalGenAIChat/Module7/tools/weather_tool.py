"""
Weather Tool

Mock implementation for Module 7 POC.
Later we'll replace this with a real Weather API.
"""

import requests

class WeatherTool:

    @property
    def name(self):
        return "get_weather"

    @property
    def description(self):
        return "Get the current weather for a city."

    @property
    def parameters(self):
        return {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name of the city."
                }
            },
            "required": ["city"]
        }

    def execute(self, arguments):

        city = arguments.get("city")

        try:

            # -----------------------------
            # Step 1 : Get Latitude & Longitude
            # -----------------------------

            geo_url = (
                "https://geocoding-api.open-meteo.com/v1/search"
                f"?name={city}&count=1"
            )

            geo_response = requests.get(
                geo_url,
                timeout=10
            )

            geo_response.raise_for_status()

            geo_data = geo_response.json()

            if "results" not in geo_data:

                return {
                    "success": False,
                    "error": f"City '{city}' not found."
                }

            location = geo_data["results"][0]

            latitude = location["latitude"]
            longitude = location["longitude"]

            # -----------------------------
            # Step 2 : Current Weather
            # -----------------------------

            weather_url = (
                "https://api.open-meteo.com/v1/forecast"
                f"?latitude={latitude}"
                f"&longitude={longitude}"
                "&current_weather=true"
            )

            weather_response = requests.get(
                weather_url,
                timeout=10
            )

            weather_response.raise_for_status()

            weather_data = weather_response.json()

            current = weather_data["current_weather"]

            return {

                "success": True,

                "city": city,

                "latitude": latitude,

                "longitude": longitude,

                "temperature": current["temperature"],

                "wind_speed": current["windspeed"],

                "wind_direction": current["winddirection"],

                "weather_code": current["weathercode"],

                "time": current["time"]
            }

        except Exception as ex:

            return {

                "success": False,

                "error": str(ex)
            }