import constants
import WeatherFetcher
import FileReaderWriter


def main():
    file_helper = FileReaderWriter.FileReaderWriter()

    # initialize the fetcher that gets data from the web API
    api_key = file_helper.readStringFromFile(constants.API_KEY_FILE)
    units = constants.UNITS
    weather_fetcher = WeatherFetcher.WeatherFetcher(api_key, units)

    # get the list of input cities
    city_list = file_helper.readObjectFromFile(constants.INPUT_CITY_FILE)

    # get the weather list for each city
    weather_data_list = []
    for city in city_list:
        weather_data_for_city = weather_fetcher.getWeather(city)
        weather_data_list.append(weather_data_for_city)

    # write the weather list into output file
    file_helper.writeObjectToFile(constants.OUTPUT_WEATHER_DATA_FILE, weather_data_list, constants.JSON_INDENT)


if __name__=='__main__':
    main()