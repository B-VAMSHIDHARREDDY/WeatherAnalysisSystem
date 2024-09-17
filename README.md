
# Weather Analysis System

## Overview

The **Weather Analysis System** is a Django-based web application that fetches real-time weather data from the WeatherAPI for a given city, processes the data to calculate weather trends (such as average temperature and humidity), and provides alerts in case of extreme weather conditions (e.g., extreme temperatures, high wind speeds, storms).

The application is designed to provide users with a detailed analysis of current weather conditions along with insights into weather patterns over the last 24 hours. Users can also be alerted to severe weather conditions like storms or high wind speeds.

## Features

- **Fetch Real-Time Weather Data:** 
   - The system uses the WeatherAPI to fetch up-to-date weather information for a specified city.
- **Data Processing & Trend Calculation:** 
   - The system calculates weather trends such as average temperature and humidity over the last 24 hours.
- **Weather Alerts:** 
   - The system generates alerts if extreme weather conditions are detected, such as high winds, extreme temperatures, heavy precipitation, or storms.
- **User-Friendly Interface:** 
   - A simple web interface where users can input a city name and get detailed weather reports and alerts.

## Technologies Used

- **Backend:** 
   - Django 5
   - Django REST Framework
   - Python3
   - WeatherAPI (for fetching weather data)
- **Frontend:** 
   - HTML5, CSS
   - JavaScript, jQuery (for AJAX requests)
- **Database:** 
   - Postgresql 

## Project Structure

```
weather_analysis/
│
├── weather/                         # Main application directory
│   ├── migrations/                  # Django migrations
│   ├── templates/                   # HTML templates
│   │   └── home.html                # Main homepage for weather input
│   ├── static/                      # Static files (CSS, JS)
│   │   ├── css/
│   │   │   └── styles.css           # Custom styles for the app
│   │   └── js/
│   │       └── weather.js           # JavaScript code for fetching and displaying weather
│   ├── services.py                  # Business logic for fetching and processing weather data
│   ├── views.py                     # Django views handling requests
│   ├── models.py                    # Django models for storing weather data
│   ├── urls.py                      # URL routing for the app
│   └── serializers.py               # Django REST Framework serializers for API endpoints
│
├── manage.py                        # Django management script
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation (this file)
```

## How to Run the Project

### Prerequisites

- Python 3
- Django 5
- WeatherAPI key (You can get it from [WeatherAPI](https://www.weatherapi.com/) after registering).

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/weather-analysis-system.git
   cd weather-analysis-system
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your WeatherAPI key and  required data in `.env`:**

   Create `.env` and add your WeatherAPI key and required data , Use sampleenv :

   ```python
   SECRET_KEY=django_secret_key
   DB_URL='postgresqlurl'
   WEATHER_API_KEY = 'your_weather_api_key_here'
   ```

5. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application in your browser:**

   Open `http://127.0.0.1:8000/` to access the home page.

### Usage

1. Enter the name of the city in the input box.
2. Click "Check Weather" to fetch and display:
   - Current weather data (temperature, humidity, wind speed, etc.)
   - Average weather trends (temperature, humidity) for the last 24 hours.
   - Any alerts for extreme weather conditions.
   
### API Endpoints

The application also exposes the following API endpoints:

- **Fetch Weather Data & Trends:**
   - URL: `/weather-analysys/?city=CityName`
   - Method: GET
   - Response:
     ```json
     {
       "current_weather": {
         "city": "Hyderabad",
         "region": "Andhra Pradesh",
         "country": "India",
         "latitude": 17.38,
         "longitude": 78.47,
         "localtime": "2024-09-17 19:16",
         "temp_c": 28.0,
         "temp_f": 82.4,
         "condition_text": "Partly cloudy",
         "humidity": 62,
         "wind_mph": 8.3,
         "pressure_mb": 1008.0,
         "feelslike_c": 31.0
       },
       "average_temperature": 28.0,
       "average_humidity": 62.0,
       "alerts": "No alerts"
     }
     ```

