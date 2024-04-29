# Introduction

According to MIT Climate Portal, the urban heat island effect is a phenomenon whereby cities experience higher air temperatures than the surrounding countryside. Scientists refer to areas afflicted by these higher temperatures as urban heat islands, and people living in these areas are particularly exposed to the effects of climate change. People living in urban heat islands are especially vulnerable to the effects of climate change. As the planet warms, urban heat islands will only intensify those higher temperatures.(https://climate.mit.edu/explainers/urban-heat-islands).

In general, certain social groups are particularly vulnerable to crises, including climate change. These vulnerable people are **children**, persons with disabilities, ethnic minorities, **migrant workers**, **displaced persons**, **older people**, and other socially marginalized groups. (https://www.worldbank.org/en/topic/social-dimensions-of-climate-change#1).

If we focus our attention on migrants (and in particular refugees) and displaced people, the UNHCR (UN Refugee Agency) states that the vast majority of refugees (approximately 78 percent) do not live in camps but in cities, and are therefore more vulnerable to the extreme heatwaves caused by climate change. In general urban locations offer more opportunities to live autonomously and find employment, but they also pose major challenges as refugees are often forced to share accommodation or live in non-functional public buildings, collective centers, slums or other types of informal settlements with substandard living conditions. (https://action.unrefugees.org/refugee-facts/camps/)

# Project Description

The aim of this project is developing an **SMS-heat-alert** and **health-check system** that **forcibly displaced population** (including internally dispaced people, refugees, asylum-seekers and other people in need of international protection that settled in **urban locations** in **developing countries** of asylum affected by **extreme heat conditions**) could benefit from by receving heat alerts in case of extreme weather conditions together with multilingual advice on practices to avoid heat-realted diseases. Moreover, they could communicate any heat-related symptoms they might experience through a multilingual SMS-form. The system would be created by and integrated with **FDP-centers** in the cities of reference where those in need could register (to create a database shared in all the urban areas) and get support, and where training to maintain the system will be delivered. The staff of these centers would consist of vulnerable people from different nationalities themselves, thus making the project multilingual, sustainable in the long-term, and scalable to other urban settlements.

It is important to note that extreme heat and its consequences on health are not the only one consequence of climate change, which include floods, draught, threat to biodiversity and agriculture, and extreme weather conditions. Moreover, forcibly displaced people do not only settle in urban areas in developing countries, but often chose least-developed countries, as well as developed ones, and they all have the same importance. Urban refugees do not only face weather-related challenges, but many more, and the UNHCR and other aid agencies cannot legally protect and support refugees dispersed in urban settings as much as in camps: it is therefore important to establish centers in urban settements where the vulnerable people feel safe to register and go to when they are in need. Collaboration between cities hosting forcibly displaced people, and partnership with NGOs and local 

# Research question

How can we identify the urban areas where to deploy the project?

# Hypotheses

We can use historical weather data and data from UNCHR to identify the areas where to deploy the project first. 

# Hypothesis notes

* Coordinates of urban settlements
* Weather Data
* Demographics of urban refugees (main focus on urban settlements of forcibly displaced population with more than 50 kids < 4 years old and 50 elderly > 60 years old. According to WHO, infants or people who are over 60 years of age or that have chronic health conditions are those most affected by heat-related diseases).

# Data sources and tools

* **UNHCR DB** https://www.unhcr.org/refugee-statistics/download/?url=0quh0N
  THe UNHCR provides a database with the demographics of forcibly displaced population including internally dispaced people, refugees, asylum-seekers and other people in need of international protection that settled in urban locations in the countries of asylum. Since there is no universal definition of urban, UNCHR classifies an urban location as a settlement with more than 5,000 inhabitants. Data for 2021 and 2022.
* **UN Historical Classification DB** https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Funstats.un.org%2Funsd%2Fmethodology%2Fm49%2Fhistorical-classification-of-developed-and-developing-regions.xlsx&wdOrigin=BROWSELINK
  UN historical classification of developing and developed countries (2021, 2022).
* **Wikipedia DB** https://en.wikipedia.org/wiki/Urban_refugee#References
  Major urban refugees settlements.
* https://open-meteo.com/en/docs/historical-weather-api
  To extract the Maximum Temperature (2 m) which is equal to the maximum temperature recorded at a height of 2 meters above the ground surface for all the identified cities from 01-01-2020 to 31-12-2023.
* https://nominatim.org/release-docs/develop/api/Overview/
  The Nominatim API was used to identify the coordinates of the urban area.
* https://umap.openstreetmap.fr/en/
  To map where the urban refugees settlements are located.
* https://www.who.int/news-room/fact-sheets/detail/climate-change-heat-and-health

# Methodology and findings

1) The **UNHCR DB** of forcibly displaced population (FDP) was used to identify the demographics of urban FDPs.
2) The **UN Historical Classification DB** was used to map the UNHCR database and identify which countries were considered **Developing** in 2021 and 2022 through a VLOOKUP in Excel. Data were cleaned in case of inconsistency (example: countries that were considered *Developing* in one of the considered years only).
3) The **Wikipedia DB** was used to identify major urban refugees settlements (web scraping on Excel). Data among the 3 databases were harmonised for Country name and ISO to have consistent data among the used database.
4) According to WHO, infants or people who are over 60 years of age or that have chronic health conditions are those most affected by heat-related diseases, therefore the dtaa were filtered by **developing countries hosting urban forcibly displaced population where babies < 4 years old and elderly > 60 years old are at least => 50** (Data filtered through Pivot Table). The .csv file **Cities.csv** was obtained.
5) The Nominatim API was used to identify coordinates of the selected urban settlements in the Cities.csv file:

       echo "lat, long, city, addresstype" > Cities_Coordinates.csv
       while read city
       do    
            result=$(curl -s "https://nominatim.openstreetmap.org/search?q=${city}&format=json" | jq '.[] | [.lat, .lon, .name, .addresstype] | @csv')
            result2=$(echo "${result//\"/}")
            echo "${result2//\/}"
       done < Cities.csv >> Cities_Coordinates.csv

The output **Cities_Coordinates.csv** was obtained.

6) The Cities_Coordinates.csv was imported in Excel and cleaned to obtain 1 value (city, locality or municipality) for each previously identified urban settlement.
7) The Cities_Coordinates.csv (in raw format from GItHub) was used to map where the urban refugees settlements are located (through *import data*):
![image](https://github.com/elenabolla/turin_crash_course-Elena/assets/167084001/719d409a-aad1-4a81-ac40-86644f6cd839)
As we could already guess, most of these urban settlements are located in Africa and the middle East.
8) The coordinates of the cities were used in **https://open-meteo.com/en/docs/historical-weather-api** to extract the Maximum Temperature (2 m) in Degree Celsius which is equal to the maximum temperature recorded at a height of 2 meters above the ground surface for all the identified cities from 01-01-2020 to 31-12-2023. The data were then cleaned in OpenRefine and imported in Excel to identify:
  * Highest temperatures 2020 - 2023 temperature variations trends,
  * Days with temperatures >= 35° Celsius (that, according to WHO, may cause heat-related diseases).
9) Data were analysed through Pivot tables and Pivot Charts to obtain what follows (Note: the number of elderly>60 and kids<4 for repeting countries such as Egypt, Iraq, Sudan, Turkey and Yemen is the same the demographic for each city was not available, therefore the country all-up was used for each city):
![image](https://github.com/elenabolla/turin_crash_course-Elena/assets/167084001/435f9e2c-76bc-48cc-8076-b11c7fb1b890)
10) **Babylon and Baghdad** (Iraq), **Khartoum and Kassala** (Sudan), **Cairo and Giza** (Egypt), **Niamei** (Niger), **Juba** (South Sudan) and **Ouagadougou** (Burkina Faso) are the urban settlements that registered the **highest temperatures** as well as the longest number of days with temperature (2 m) > 35° Celsius, the level that WHO identifies are responsible for heat-related diseases.
All settlements had over 100 days above 35° Celsius in all the considered years (2020, 2021, 2022, 2023):
![image](https://github.com/elenabolla/turin_crash_course-Elena/assets/167084001/d1604d62-26de-4379-96bf-666dc1ee8a41)
Moreover, they all score amonge the top 20 of urban settlements with highest temperatures in 2023:
![image](https://github.com/elenabolla/turin_crash_course-Elena/assets/167084001/6bc27da0-9a76-4797-be1c-67d5a066cbec)
![image](https://github.com/elenabolla/turin_crash_course-Elena/assets/167084001/80112929-6b65-4b9b-97bb-c9e2233f2ba2)




