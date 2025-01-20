import requests

def get_weather(city):
    api_key = "dummy_api_key"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
