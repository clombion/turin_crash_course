def fetch_weather_data(city_name, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={edf0946bfb5d6100cb23743b55e6163a}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error fetching data:', response.status_code)
        return None
