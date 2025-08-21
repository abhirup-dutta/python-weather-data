import json

import WeatherFetcher
import FileReaderWriter

def main():
    api_key = "09fc6842e6f70b6eb16937894df3657f"
    units = "metric"
    weather_fetcher = WeatherFetcher.WeatherFetcher(api_key, units)

    file_helper = FileReaderWriter.FileReaderWriter()
    cities = file_helper.readFile('cities.json')
    print(cities)
    weather_data = []
    for city in cities:
        print(city)
        weather_result = weather_fetcher.getWeather(city)
        print(weather_result)
        weather_data.append(weather_result)
    weather_data_json = json.dumps(weather_data)
    file_helper.writeToFile('weather.json', weather_data_json)


if __name__=='__main__':
    main()