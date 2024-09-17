from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import WeatherService

class WeatherTrendsAndAlerts(APIView):
    def get(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response({"error": "City is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create an instance of WeatherService
            weather_service = WeatherService(city)

            # Fetch and save weather data
            weather = weather_service.fetch_and_save_weather_data()

            # Calculate weather trends
            avg_temperature, avg_humidity = weather_service.calculate_weather_trends()

            # Generate weather alerts
            alerts = weather_service.generate_weather_alerts()

            response_data = {
                "current_weather": weather,
                "average_temperature": avg_temperature,
                "average_humidity": avg_humidity,
                "alerts": alerts if alerts else "No alerts"
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
