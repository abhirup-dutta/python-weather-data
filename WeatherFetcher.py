import requests

import constants

class WeatherFetcher:

    def __init__(self, api_key, units):
        self.api_key = api_key
        self.units = units
        self.api_template = constants.WEATHER_API_TEMPLATE

    def getWeather(self, city):
        prepared_request_api = self.api_template.format(city, self.units, self.api_key)
        response_json = requests.get(prepared_request_api).json()
        summary = response_json['weather'][0]['main']
        temperature = response_json['main']['temp']
        humidity = response_json['main']['humidity']
        return self._pythonObjectify(city, summary, temperature, humidity)

    def _pythonObjectify(self, city, summary, temperature, humidity):
        return {
            "city" : city,
            "summary" : summary,
            "temperature" : temperature,
            "humidity" : humidity
        }


