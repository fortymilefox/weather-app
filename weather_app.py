import requests
import sys

# Import API key from config file
try:
    from config import API_KEY
except ImportError:
    print("Error: config.py file not found!")
    print("Please create a config.py file with your API_KEY")
    sys.exit(1)

# OpenWeatherMap API base URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """
    Fetch weather data for a given city from OpenWeatherMap API.
    
    Args:
        city_name (str): Name of the city to get weather for
        
    Returns:
        dict: Weather data if successful, None if failed
    """
    # Build the complete URL with parameters
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'imperial'  # Use metric units (Celsius)
    }
    
    try:
        # Make the API request
        response = requests.get(BASE_URL, params=params)
        
        # Check if request was successful
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Error: City '{city_name}' not found.")
            return None
        else:
            print(f"Error: Unable to fetch weather data (Status code: {response.status_code})")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error: Network problem occurred - {e}")
        return None

def display_weather(weather_data):
    """
    Display weather information in a formatted way.
    
    Args:
        weather_data (dict): Weather data from API
    """
    # Extract relevant information from the JSON response
    city = weather_data['name']
    country = weather_data['sys']['country']
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']
    
    # Display the weather information
    print("\n" + "="*50)
    print(f"Weather in {city}, {country}")
    print("="*50)
    print(f"Temperature: {temp}°F (Feels like: {feels_like}°F)")
    print(f"Conditions: {description.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print("="*50 + "\n")

def main():
    """
    Main function to run the weather app.
    """
    print("Welcome to the Weather App!")
    print("="*50)
    
    # Get city name from user
    city = input("Enter city name: ").strip()
    
    # Validate input
    if not city:
        print("Error: City name cannot be empty!")
        return
    
    print(f"\nFetching weather data for {city}...")
    
    # Get weather data
    weather_data = get_weather(city)
    
    # Display results if data was retrieved successfully
    if weather_data:
        display_weather(weather_data)
    else:
        print("Failed to retrieve weather data. Please try again.")

if __name__ == "__main__":
    main()
