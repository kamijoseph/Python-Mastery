import requests

class WeatherTracker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/"
        
    def fetch_weather(self, location):
        url = f"{self.base_url}weather?q={location}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json
            weather_info = {
                'location': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather_info
        else:
            return None