import requests
import json

class WeatherFetcher:

    def __init__(self, api_key, units):
        self.api_key = api_key
        self.units = units
        self.api_template = "https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}"

    def getWeather(self, city):
        prepared_request_api = self.api_template.format(city, self.units, self.api_key)
        response_json = requests.get(prepared_request_api).json()
        summary = response_json['weather'][0]['main']
        temperature = response_json['main']['temp']
        humidity = response_json['main']['humidity']
        return self._jsonify(summary, temperature, humidity)

    def _jsonify(self, summary, temperature, humidity):
        weather_results = {
            "summary" : summary,
            "temperature" : temperature,
            "humidity" : humidity
        }
        prepared_json = json.dumps(weather_results)
        return prepared_json


