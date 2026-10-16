import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()

        print(f"\nCity: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
    elif response.status_code == 401:
        print("API key invalid or not activated yet.")
    elif response.status_code == 404:
        print("City not found.")
    else:
        print(f"Request failed: {response.status_code}")

city = input("Enter city name: ").strip()

if API_KEY and city:
    get_weather(city)
else:
    print("API key or city name is missing.")