import requests
import sys

#Import API Key from config
try:
    from config import API_KEY
except ImportError:
    print("Error: config.py not found")
    print("Create a config.py file")
    sys.exit(1)

#OpenWeatherMap API base URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
            'q': city_name,
            'appid': API_KEY
            'units':'imperial'
            }

