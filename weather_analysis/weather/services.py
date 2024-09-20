import requests
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .models import WeatherData
from django.db import models

class WeatherService:
    def __init__(self, city):
        self.city = city
        self.weather_data = None

    def fetch_and_save_weather_data(self):
        api_key = settings.WEATHER_API_KEY
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={self.city}&aqi=no"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Failed to fetch data")

        data = response.json()

        weather = {
            'city': data['location']['name'],
            'region': data['location']['region'],
            'country': data['location']['country'],
            'latitude': data['location']['lat'],
            'longitude': data['location']['lon'],
            'localtime': data['location']['localtime'],
            'temp_c': data['current']['temp_c'],
            'temp_f': data['current']['temp_f'],
            'condition_text': data['current']['condition']['text'],
            'condition_code': data['current']['condition']['code'],
            'humidity': data['current']['humidity'],
            'wind_mph': data['current']['wind_mph'],
            'wind_kph': data['current']['wind_kph'],
            'pressure_mb': data['current']['pressure_mb'],
            'precip_mm': data['current']['precip_mm'],
            'cloud': data['current']['cloud'],
            'feelslike_c': data['current']['feelslike_c'],
            'feelslike_f': data['current']['feelslike_f'],
            'uv': data['current']['uv']
        }

        # Save data to DB
        self.weather_data = WeatherData(**weather)
        self.weather_data.save()

        return weather

    def calculate_weather_trends(self):
        past_24_hours = timezone.now() - timedelta(hours=24)
        weather_data = WeatherData.objects.filter(city=self.weather_data.city, localtime__gte=past_24_hours)

        if not weather_data.exists():
            return None, None

        avg_temperature = weather_data.aggregate(models.Avg('temp_c'))['temp_c__avg']
        avg_humidity = weather_data.aggregate(models.Avg('humidity'))['humidity__avg']

        return round(avg_temperature,2), round(avg_humidity,3)

    def generate_weather_alerts(self):
        if not self.weather_data:
            raise Exception("Weather data is not available")

        alerts = []

        # Check for extreme temperature
        if self.weather_data.temp_c > 40 or self.weather_data.temp_c < -10:
            alerts.append("Extreme temperature!")

        # Check for high wind speeds
        if self.weather_data.wind_mph > 50:
            alerts.append("High wind speed!")

        # Check for heavy precipitation
        if self.weather_data.precip_mm > 10:
            alerts.append("Heavy precipitation!")

        # Check for severe weather conditions
        if "storm" in self.weather_data.condition_text.lower():
            alerts.append("Storm warning!")

        return alerts
