# weather_checker.py
# Author: hajar1010
# Description: A command-line app that shows the current weather for a given city.
import requests

API_KEY = "94244daaab1b75442593070b0e912584"
while True:
    city = input("Enter your city : ")
    if city == "":
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        print("Request successful!")
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition.capitalize()}")
        print(f"Humidity: {humidity}%\n")
    else:
        print(f"Error: {response.status_code}")

    again = input("Check another city? (yes/no): ").strip().lower()
    if again != "yes":
        break