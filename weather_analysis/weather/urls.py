from django.urls import path
from django.views.generic import TemplateView
from .views import WeatherTrendsAndAlerts

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('weather-analysys/', WeatherTrendsAndAlerts.as_view(), name='weather_analysys'),
]
