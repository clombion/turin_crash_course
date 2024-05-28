if city_data:
    weather_info = {
        'City': city_data['name'],
        'Country': city_data['sys']['country'],
        'Temperature (C)': city_data['main']['temp'] - 273.15,  # Convert Kelvin to Celsius
        'Humidity (%)': city_data['main']['humidity'],
        'Wind Speed (m/s)': city_data['wind']['speed']
    }
