# python-weather-data
Reads a file of locations, gets weather data from the web, and writes to another file

## Checking the constants
Go to constants.py and modify constants

This includes units such as

UNITS = 'metric' or

UNITS = 'imperial'



## Getting Key from Web API
Here, we are using https://openweathermap.org/

Sign up and get an API key

Fill this in './api.key' (or the value of API_KEY_FILE in constants.py)

## Input cities
Json object [ 'city1', 'city2' ] as shown in './cities.json' (or the value of INPUT_CITY_FILE in ./constants.py)

## Output Data
[

    {

        "city": "Buenos Aires",
        
        "summary": "Clear",
        
        "temperature": 13.19,
        
        "humidity": 74
    
    },
    
    {
    
        "city": "Nuuk",
        
        "summary": "Clouds",
        
        "temperature": 13.34,
        
        "humidity": 76
    
    }

]

as shown in './weather.json' (or the value of OUTPUT_WEATHER_DATA_FILE in ./constants.py)
