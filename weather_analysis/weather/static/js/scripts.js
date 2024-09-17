$(document).ready(function () {
    $('#fetch-weather').click(function () {
        var city = $('#city-input').val().trim();
        if (city === "") {
            alert("Please enter a city name.");
            return;
        }

        $.ajax({
            url: '/weather-analysys/',  // Django API URL
            type: 'GET',
            data: { city: city },
            success: function (data) {
                // Populate weather data
                $('#city-name').text(data.current_weather.city);
                $('#region').text(data.current_weather.region);
                $('#country').text(data.current_weather.country);
                $('#localtime').text(data.current_weather.localtime);
                $('#temp_c').text(data.current_weather.temp_c);
                $('#temp_f').text(data.current_weather.temp_f);
                $('#feelslike_c').text(data.current_weather.feelslike_c);
                $('#condition_text').text(data.current_weather.condition_text);
                $('#humidity').text(data.current_weather.humidity);
                $('#wind_mph').text(data.current_weather.wind_mph);
                $('#wind_kph').text(data.current_weather.wind_kph);
                $('#pressure_mb').text(data.current_weather.pressure_mb);
                $('#uv').text(data.current_weather.uv);

                // Populate trends
                $('#avg_temp').text(data.average_temperature);
                $('#avg_humidity').text(data.average_humidity);

                // Populate alerts
                var alerts = data.alerts || [];
                var alertsList = $('#alerts-list');
                alertsList.empty(); // Clear existing alerts
                if (alerts.length > 0) {
                    alerts.forEach(function(alert) {
                        alertsList.append('<li style="color: red;">' + alert + '</li>');
                    });
                } else {
                    alertsList.append('<li>No alerts</li>');
                }

                // Update weather icon based on condition
                var condition = data.current_weather.condition_text.toLowerCase();
                var iconClass = '';
                if (condition.includes('sunny')) {
                    iconClass = 'fas fa-sun';
                } else if (condition.includes('cloudy')) {
                    iconClass = 'fas fa-cloud';
                } else if (condition.includes('rain')) {
                    iconClass = 'fas fa-cloud-showers-heavy';
                } else if (condition.includes('snow')) {
                    iconClass = 'fas fa-snowflake';
                }
                $('.weather-icon').removeClass().addClass('weather-icon ' + iconClass);

                // Show weather details with a slide-in effect
                $('.weather-container').slideDown('slow');
            },
            error: function () {
                alert("Error fetching weather data. Please try again.");
            }
        });
    });
});
