import requests
import json
import datetime

# Function to fetch data from OpenWeatherMap API
def fetch_data_openweathermap(api_url, latitude, longitude, api_key):
    # Set the date for which you want the data (e.g., 7 days ago)
    date = datetime.datetime.now() - datetime.timedelta(days=7)
    timestamp = int(date.timestamp())
    
    params = {
        "lat": latitude,
        "lon": longitude,
        "dt": timestamp,
        "appid": api_key
    }
    
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data from OpenWeatherMap (Status code: {response.status_code})")
        return None

# Main function to orchestrate data fetching and saving
def main():
    # Define OpenWeatherMap API details
    openweathermap_api_url = "http://api.openweathermap.org/data/2.5/onecall/timemachine"
    api_key = "ef7da6e160c7e355073d9ececc7a5a2c"  # Replace with your actual OpenWeatherMap API key
    latitude = "d24e712ca4474c57758d4f3aead5f197"  # Replace with the latitude of the location
    longitude = "ed860f76503f457deea1b056e28dbdb9"  # Replace with the longitude of the location
    
    # Fetch data from OpenWeatherMap
    openweathermap_data = fetch_data_openweathermap(openweathermap_api_url, latitude, longitude, api_key)
    
    # Save OpenWeatherMap data to a JSON file if fetched successfully
    if openweathermap_data:
        with open('data/raw_data/urban_heat_islands_openweathermap.json', 'w') as json_file:
            json.dump(openweathermap_data, json_file, indent=4)
        print("OpenWeatherMap data successfully retrieved and saved to urban_heat_islands_openweathermap.json")

# Run the main function
if __name__ == "__main__":
    main()

