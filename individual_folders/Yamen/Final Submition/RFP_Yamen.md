# Mitigating Urban Heat Islands for Vulnerable Populations in Developing Countries

### Introduction
The term "urban heat island" refers to a phenomenon that occurs when temperatures in urban areas are higher than those in the areas that surround them (suburban area). The gradually increase in temperature in urban areas would affect many vulnerable communities around the world including homeless and refugees who lack adequate shelter and resources to cope up with extreme heat especially in the MENA region.

### Objective
The aim of the assignment is to identify urban areas predominantly affected by the urban heat island effect, with a specific emphasis on locales inhabited by vulnerable populations especially refugee. 

### Research Questions
Which urban areas host the most vulnerable refugee populations? How can we reduce the impact of urban heat islands on these populations?

### List of dataset/API used
1. [UNHCR Statistical 2021 | Database](https://data.un.org/Data.aspx?q=refugee&d=UNHCR&f=indID:Type-Ref&c=0,1,2,3,4,5,6&s=yr:desc,asyEngName:asc,oriEngName:asc&v=1#UNHCR)
2. [World Bank Analytical Classifications | Database](https://integratedintl-my.sharepoint.com/personal/msadmin_integratedinternational_org/Documents/datatopics.worldbank.org/world-development-indicators/the-world-by-income-and-region.html)
3. [Global Urban Heat Island | Database](https://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013/data-download)
4. [Open-Meteo (API)](https://open-meteo.com/en/docs)



### Methodology 
The proposed assignment will adhere to the following structured process:

**1. Country Level Mapping (Master Table):**

Refugees are inclined to reside predominantly in urban areas. Communities accommodating a large refugee population tend to face Urban Heat Island (UHI) effects, largely due to the increased density of refugees and urbanization within the country. Economic status is also a crucial factor in determining vulnerability. For example, Turkey hosts a significant number of refugees but maintains an upper-middle economic status, with a considerable number of urban areas.
| Column                                    | Description                                                                                                                                                     | Source                                     | Aim                                                                |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|--------------------------------------------------------------------|
| Country of residence                      | All countries across the world                                                                                                                                  | UNHCR Statistical Database 2021            |                                 Used as Primery Key                    |
| Total refugees and people in refugee-like situation | The category of people in refugee-like situations is descriptive in nature and includes groups of persons who are outside their country or territory of origin and who face protection risks similar to those of refugees, but for whom refugee status has, for practical or other reasons, not been ascertained. | UNHCR Statistical Database 2021            | Mapping the number of refugees in countries across the globe       |
| Class                                     | Low income (L), Lower middle income (LM), Upper middle income (UM), High income (H)                                                                              | World Bank Analytical Classifications Database | To classify data by income level to identify the most fragile communities against UHI |
| Urban Area                                | Calculated field showing the number of urban areas in square kilometers                                                                                         | Global Urban Heat Island Data              |                                                                    |
| Num. of urban                             | Calculated field showing total urban areas in square kilometers                                                                                                 | Global Urban Heat Island Data              |                                                                    |
| Ratio                                     | Total refugees/Num. of urban                                                                                                                                     |                                            | To analyze the distribution of refugees in urban areas             |

As a result, we can now make a clear decision to prioritize low to lower-middle-income countries with a high refugee ratio for the start of our project.

| Row Labels         | Refugee in 2021 | Economic Status | SUM URBAN AREAS KM2 | NUM OF URBAN | RATIO  |
|--------------------|-----------------|-----------------|----------------------|--------------|--------|
| **Lebanon**           | 856,758         | LM              | 2,209                | 11           | 77,887 |
| **Jordan**             | 708,308         | LM              | 3,102                | 12           | 59,026 |
| **Uganda**             | 1,475,311       | L               | 1,396                | 61           | 24,185 |
| **Sudan**              | 1,389,218       | L               | 6,146                | 66           | 21,049 |
| Iraq               | 272,215         | UM              | 10,314               | 21           | 12,963 |
| Turkiye            | 3,696,831       | UM              | 43,740               | 342          | 10,809 |
| Chad               | 508,304         | L               | 1,571                | 53           | 9,591  |
| Pakistan           | 1,438,523       | LM              | 26,088               | 174          | 8,267  |
| Rwanda             | 122,806         | L               | 511                  | 15           | 8,187  |
| Bangladesh         | 889,775         | LM              | 10,063               | 129          | 6,897  |
| Kenya              | 466,286         | LM              | 3,549                | 75           | 6,217  |
| Niger              | 245,449         | L               | 1,362                | 40           | 6,136  |
| Iran, Islamic Rep. | 800,025         | LM              | 60,296               | 136          | 5,883  |
| Burundi            | 76,837          | L               | 563                  | 15           | 5,122  |
| Egypt, Arab Rep.   | 277,665         | LM              | 12,997               | 62           | 4,478  |
| Djibouti           | 22,123          | LM              | 160                  | 5            | 4,425  |
| Yemen, Rep.        | 129,001         | L               | 4,227                | 31           | 4,161  |
| Tanzania           | 202,635         | LM              | 3,319                | 56           | 3,618  |
| Mauritania         | 99,056          | LM              | 978                  | 32           | 3,096  |
| Congo, Dem. Rep.   | 519,819         | L               | 9,315                | 176          | 2,954  |
| Cameroon           | 446,101         | LM              | 4,651                | 175          | 2,549  |
| Ethiopia           | 782,896         | L               | 6,788                | 387          | 2,023  |
| Malaysia           | 131,094         | UM              | 14,442               | 70           | 1,873  |

**2.	Urban Area Level**

Now that we've identified the communities most in need to kickstart our project, it's crucial to intensify our focus on prioritizing countries and pinpointing specific urban areas for our research. In this phase, we delve deeper into urban environments and temperature dynamics to determine where to begin our quest for impactful grassroots solutions. 
Starting by filtering the Global Urban Heat Island Data to keep only the urban areas that are related to Lebanon, Sudan, Jordan and Uganda (N=150)

| Column          | Description                                                                                 | Source                          | Aim                                           |
|-----------------|---------------------------------------------------------------------------------------------|---------------------------------|----------------------------------------------|
| Country         |                                                                                             | Global Urban Heat Island Data   | Foreign key for Master table                 |
| ISOURBID        | Unique ID created by concatenating ISO3 code and Urban ID number (URBID)                    | Global Urban Heat Island Data   |                                               |
| ISO3            | International Standards Organization three-letter country code                              | Global Urban Heat Island Data   |                                               |
| URBID           | Urban ID number (unique within country)                                                     | Global Urban Heat Island Data   |                                               |
| NAME            | City or urban agglomeration name                                                            | Global Urban Heat Island Data   |                                               |
| SCHNM           | City or urban agglomeration name in CAPS, concatenated, and without accents                 | Global Urban Heat Island Data   |                                               |
| SQKM_FINAL      | Area of urban extent in square kilometers                                                   | Global Urban Heat Island Data   |                                               |
| LATITUDE        | Latitude of centroid of urban extent in decimal degrees                                     | Global Urban Heat Island Data   | Used to extract temperature daylight data on a daily basis |
| LONGITUDE       | Longitude of centroid of urban extent in decimal degrees                                    | Global Urban Heat Island Data   | Used to extract temperature daylight data on a daily basis |
| temp. avg.      | Reference the Jupyter notebook                                                              | Calculated via Open-Meteo       |                                               |


**3. Daily Temperature Series Retrieval**

Utilizing the Openmeteo API, I developed a loop to extract maximum temperature (2m) data on a daily basis for urban areas listed in Table 2. Initially, the objective was to gather data spanning the past five years. However, due to API limitations, only data from the previous 15 days could be retrieved. Despite encountering issues where the API crashed and refused retrieval requests, I successfully obtained data using the following code snippet:

```python
import openmeteo_requests
import requests_cache
import time
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Define the API endpoint and parameters
url = "https://archive-api.open-meteo.com/v1/archive"
start_date = "2020-01-01"
end_date = "2024-05-31"
daily_variables = ["temperature_2m_max", "daylight_duration"]

# Read input CSV file
input_file = 'coordinates.csv'
output_file = 'updated_coordinates.csv'

# Read coordinates from CSV and process each one
coordinates_df = pd.read_csv(input_file)

# Initialize lists to hold new data
all_temperature_2m_max = []
all_daylight_duration = []

for index, row in coordinates_df.iterrows():
    latitude = row['latitude']
    longitude = row['longitude']
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": daily_variables
    }
    
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    
    # Extract and print some meta information
    print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+2 {response.UtcOffsetSeconds()} s")
    
    # Process daily data
    daily = response.Daily()
    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
    daily_daylight_duration = daily.Variables(1).ValuesAsNumpy()
    
    # Calculate the average values for the given date range
    avg_temp_max = daily_temperature_2m_max.mean() if len(daily_temperature_2m_max) > 0 else None
    avg_daylight = daily_daylight_duration.mean() if len(daily_daylight_duration) > 0 else None
    
    # Append to lists
    all_temperature_2m_max.append(avg_temp_max)
    all_daylight_duration.append(avg_daylight)
    
    # To avoid hitting the API rate limit
    time.sleep(1)  # Sleep for 1 second between requests

# Add new data as columns to the original DataFrame
coordinates_df['avg_temperature_2m_max'] = all_temperature_2m_max
coordinates_df['avg_daylight_duration'] = all_daylight_duration

# Save the updated DataFrame to a new CSV file
coordinates_df.to_csv(output_file, index=False)
print(f"Data saved to {output_file}")

```

The extracted data was organized and aggregated using a Pivot table, which was then added to Table 2.

**4.	Visual mapping**

I developed a [comprehensive dashboard](https://app.powerbi.com/view?r=eyJrIjoiZTk0MjMxOGUtZWY1Ny00NTNiLWE1OGItNmU3NTFlYTNhYzA3IiwidCI6IjllMjQ4ZWRlLTFiODAtNDA5OS05ZTM1LTk1NjdjOGUzZDM5ZCIsImMiOjl9) 
 aimed at providing succinct answers to key questions, facilitating decision-making processes for stakeholders. This dashboard offers clear insights into various aspects, enabling decision-makers to strategically plan future interventions.

### Findings:
**•	Sudan is Priority**
 
Despite being considered a haven for refugees from 13 African nations seeking refuge from conflict, 50% of urban areas in Sudan experience relatively high temperatures, reaching around 40°C. The significant refugee population in Sudan, totaling 1,068,339 according to UN data in 2021, adds to the complexity of the situation. With the ongoing crises exacerbating the challenges, there's an urgent need for actionable and rapid solutions to address the Urban Heat Island (UHI) issue in Sudan.

**•	Coastal Area on the risk**
 
In Aqaba, Jordan, the continuous rise in temperature poses a heightened risk of floods and tsunamis, particularly due to its coastal location.

**•	More data is still needed.**
The lack of accurate and essential information, such as population figures and details about new urban areas, complicates the situation in developing countries. Advocating for a unified data structure across different stakeholders will help researchers produce more effective solutions.


**Solution Development**

**•	Solar-Powered Cooling Stations:** Establish solar-powered cooling stations in key urban areas. These stations can provide a cool, shaded place for people to rest, charge their phones, and access clean drinking water. This solution is ideal for the MENA region and Africa, taking advantage of the abundant sunlight to offer relief from high temperatures and improve quality of life.
**•	Community-Driven Reforestation Programs:** Launch community-led reforestation projects in urban and peri-urban areas. By involving local residents and refugees, these programs can increase tree cover, providing natural cooling and fostering a sense of community ownership and responsibility for the environment.
**•	Climate-Resilient Infrastructure:** Develop climate-resilient infrastructure such as permeable pavements and green roofs that integrate local materials and traditional building practices. These can help manage stormwater, reduce flooding, and lower temperatures, making urban areas more adaptable to extreme weather conditions.







