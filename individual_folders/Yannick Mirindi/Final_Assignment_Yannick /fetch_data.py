import requests
import json
import os

# Define the API endpoint and parameters
api_url = "https://api.nasa.gov/planetary/earth/assets"
params = {
    "lon": "10.0", # Example longitude, replace with your coordinates
    "lat": "20.0", # Example latitude, replace with your coordinates
    "begin": "2023-01-01",
    "end": "2023-12-31",
    "dim": "0.1", # Dimension of the image
    "api_key": "YOUR_API_KEY"
}

# Make API request
response = requests.get(api_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Ensure the data directory exists
    if not os.path.exists('data/raw_data'):
        os.makedirs('data/raw_data')
    
    # Save the data to a JSON file
    with open('data/raw_data/urban_heat_islands.json', 'w') as json_file:
        json.dump(data, json_file)
        
    print("Data successfully retrieved and saved to urban_heat_islands.json.")
else:
    print("Error: Unable to fetch data.")
