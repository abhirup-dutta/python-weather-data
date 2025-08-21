import WeatherFetcher

def main():
    api_key = "09fc6842e6f70b6eb16937894df3657f"
    units = "metric"
    city = "Hanoi"
    weatherFetcher = WeatherFetcher.WeatherFetcher(api_key, units)
    weather_results = weatherFetcher.getWeather(city)
    print(weather_results)

if __name__=='__main__':
    main()