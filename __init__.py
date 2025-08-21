import constants
import WeatherFetcher
import FileReaderWriter


def main():
    file_helper = FileReaderWriter.FileReaderWriter()

    api_key = file_helper.readStringFromFile(constants.API_KEY_FILE)
    units = constants.UNITS
    weather_fetcher = WeatherFetcher.WeatherFetcher(api_key, units)

    cities = file_helper.readObjectFromFile(constants.INPUT_CITY_FILE)
    print(cities)

    weather_data = []
    for city in cities:
        print(city)
        weather_result = weather_fetcher.getWeather(city)
        print(weather_result)
        weather_data.append(weather_result)

    file_helper.writeObjectToFile(constants.OUTPUT_WEATHER_DATA_FILE, weather_data, 4)


if __name__=='__main__':
    main()