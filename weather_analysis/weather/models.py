from django.db import models

class WeatherData(models.Model):
    # Location Info
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    localtime = models.DateTimeField()

    # Current Weather Info
    temp_c = models.FloatField()
    temp_f = models.FloatField()
    condition_text = models.CharField(max_length=100)
    condition_code = models.IntegerField()

    # Additional Weather Parameters
    humidity = models.IntegerField()
    wind_mph = models.FloatField()
    wind_kph = models.FloatField()
    pressure_mb = models.FloatField()
    precip_mm = models.FloatField()
    cloud = models.IntegerField()
    feelslike_c = models.FloatField()
    feelslike_f = models.FloatField()
    uv = models.FloatField()

    def __str__(self):
        return f"Weather in {self.city} ({self.localtime})"
