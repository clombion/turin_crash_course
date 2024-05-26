# Introduction

Urban Heat Islands (UHIs) are a growing concern in cities worldwide, particularly in developing countries where rapid urbanization often outpaces the implementation of sustainable urban planning practices. UHIs result from the concentration of human activities and infrastructure, leading to significantly higher temperatures in urban areas compared to their rural surroundings. This phenomenon exacerbates the effects of climate change, contributing to health risks, increased energy consumption, and diminished quality of life, especially for vulnerable populations who typically lack adequate resources to cope with extreme heat.

The Civic Literacy Initiative (CLI) is dedicated to fostering sustainable and inclusive urban development. Through our Cool Communities Initiative (CCI), we aim to mitigate the impact of UHIs in developing countries by implementing a comprehensive approach that combines green infrastructure, community engagement, and innovative technologies. By targeting urban areas with high UHI intensity and socio-economically disadvantaged populations, CCI seeks to enhance climate resilience, reduce urban temperatures, and promote healthier living environments.
This proposal outlines a detailed plan for the Cool Communities Initiative, including specific interventions, methodologies, and expected outcomes. We seek to collaborate with local governments, community organizations, research institutions, and private sector partners to create cooler, more livable urban spaces that can serve as models for sustainable urban development in other regions.

For more information on the impact of UHIs and the importance of mitigating their effects, please refer to the following resources:
•	Environmental Protection Agency (EPA) on Urban Heat Islands https://www.epa.gov/heat-islands 
•	World Health Organization (WHO) on Climate Change and Health https://www.who.int/health-topics/climate-change
•	United Nations (UN) Sustainable Development Goals https://www.un.org/sustainabledevelopment/sustainable-cities/
 

# Project Description

The Cool Communities Initiative (CCI) is an ambitious project designed to address the pressing issue of Urban Heat Islands (UHIs) in developing countries. UHIs exacerbate the effects of climate change by increasing urban temperatures, which in turn heightens public health risks, energy consumption, and environmental stress. Vulnerable populations, often living in densely populated and under-resourced areas, are disproportionately affected by these conditions.
The initiative focuses on implementing a multifaceted strategy to mitigate the UHI effect through sustainable and innovative solutions. These solutions include green infrastructure, such as green roofs and urban forestry, cool pavements, and water features, which are scientifically proven to reduce urban temperatures. Additionally, CCI emphasizes the importance of community engagement and education, ensuring that local populations are actively involved in and benefit from the interventions.

# Research questions.

How can targeted green infrastructure and community engagement strategies effectively mitigate the Urban Heat Island (UHI) effect in vulnerable urban areas of developing countries, and what are the measurable impacts on public health, energy consumption, and overall climate resilience?

# Hypothesis:
Implementing targeted green infrastructure interventions and fostering community engagement will lead to a significant reduction in urban temperatures and an improvement in public health outcomes in vulnerable urban areas of developing countries.
Explanation:
The hypothesis posits that by strategically implementing green infrastructure interventions, such as green roofs, urban forestry, and cool pavements, in conjunction with robust community engagement strategies, it will be possible to effectively mitigate the Urban Heat Island (UHI) effect. Green infrastructure, such as vegetation and reflective surfaces, has been demonstrated to absorb heat, provide shade, and enhance natural cooling processes, thereby lowering surface temperatures in urban areas. Moreover, community engagement initiatives empower local residents to participate in decision-making processes, contribute to project planning and implementation, and take ownership of green spaces, fostering a sense of pride and stewardship within communities.

# Expected Outcomes:
1.	**Reduction in Urban Temperatures:** It is anticipated that the implementation of green infrastructure interventions will lead to a measurable decrease in urban temperatures, particularly in UHI hotspots within vulnerable urban areas.
2.	**Improvement in Public Health:** By lowering ambient temperatures and providing cooler microclimates, UHI mitigation strategies are expected to result in a reduction in heat-related illnesses and respiratory conditions among vulnerable populations.
3.	**Enhanced Climate Resilience:** The combination of green infrastructure and community engagement is expected to enhance the resilience of vulnerable communities to the impacts of climate change, including extreme heat events.
4.	**Positive Social and Economic Impacts:** Community engagement initiatives are expected to foster social cohesion, empower marginalized communities, and create economic opportunities, thereby contributing to overall socio-economic development.
   
# Validation:
The hypothesis will be tested through rigorous monitoring and evaluation of UHI mitigation projects implemented as part of the Cool Communities Initiative. Data on urban temperatures, public health indicators, community engagement metrics, and socio-economic factors will be collected and analyzed to assess the effectiveness of the interventions and validate the hypothesis. Additionally, comparative studies and case analyses will be conducted to examine the outcomes of similar projects implemented in different contexts, further validating the hypothesis and identifying best practices for UHI mitigation in developing countries.

# Hypothesis notes

1.	**Focus on Green Infrastructure:** The hypothesis emphasizes the importance of green infrastructure as a primary strategy for mitigating the Urban Heat Island (UHI) effect. This includes interventions such as green roofs, urban forestry, and cool pavements, which are designed to absorb heat, provide shade, and enhance natural cooling processes in urban areas.
2.	**Community Engagement as a Key Component:** Recognizing the significance of community involvement, the hypothesis highlights the role of community engagement in fostering ownership, participation, and stewardship of green spaces. By empowering local residents to contribute to decision-making processes and project implementation, community engagement is expected to enhance the effectiveness and sustainability of UHI mitigation efforts.
3.	**Expected Outcomes:** The hypothesis predicts specific outcomes resulting from the implementation of green infrastructure and community engagement strategies, including a reduction in urban temperatures, improvement in public health outcomes, and enhanced climate resilience among vulnerable populations in developing countries.
4.	**Potential Social and Economic Impacts:** Beyond environmental benefits, the hypothesis suggests that UHI mitigation initiatives have the potential to generate positive social and economic impacts. These may include increased social cohesion, empowerment of marginalized communities, and the creation of economic opportunities, contributing to overall socio-economic development.

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
7) The Cities_Coordinates.csv (in raw format from GItHub) was used in Umap to map where the urban refugees settlements are located (through *import data*):
![image](https://github.com/elenabolla/turin_crash_course-Elena/assets/167084001/719d409a-aad1-4a81-ac40-86644f6cd839)
As we could already guess, most of these urban settlements are located in Africa and the middle East.
8) The coordinates of the cities were used in **https://open-meteo.com/en/docs/historical-weather-api** to extract the Maximum Temperature (2 m) in Degree Celsius which is equal to the maximum temperature recorded at a height of 2 meters above the ground surface for all the identified cities from 01-01-2020 to 31-12-2023. The data were then cleaned in OpenRefine and imported in Excel to identify:
  * Highest temperatures 2020 - 2023 temperature variations trends,
  * Days with temperatures >= 35° Celsius (that, according to WHO, may cause heat-related diseases).
9) Data were analysed through Pivot tables and Pivot Charts to obtain what follows (Note: the number of elderly>60 and kids<4 for repeting countries such as Egypt, Iraq, Sudan, Turkey and Yemen is the same the demographic for each city was not available, therefore the country all-up was used for each city):
![image](https://github.com/elenabolla/turin_crash_course-Elena/assets/167084001/435f9e2c-76bc-48cc-8076-b11c7fb1b890)
10) **Babylon and Baghdad** (Iraq), **Khartoum and Kassala** (Sudan), **Cairo and Giza** (Egypt), **Niamei** (Niger), **Juba** (South Sudan) and **Ouagadougou** (Burkina Faso) are the urban settlements that registered the **highest temperatures** as well as the longest number of days with temperature (2 m) > 35° Celsius, the level that WHO identifies are responsible for heat-related diseases.

All considered countries, and in particular Egypt and Iraq, have an all-up number of urban refugees < 4 years old and > 60 years old that is greater than **100,000**.

All settlements had **over 100 days above 35° Celsius** in all the considered years (2020, 2021, 2022, 2023):
![image](https://github.com/elenabolla/turin_crash_course-Elena/assets/167084001/d1604d62-26de-4379-96bf-666dc1ee8a41)
Moreover, they all score among the top 20 of urban settlements with highest temperatures in 2023:
![image](https://github.com/elenabolla/turin_crash_course-Elena/assets/167084001/6bc27da0-9a76-4797-be1c-67d5a066cbec)
![image](https://github.com/elenabolla/turin_crash_course-Elena/assets/167084001/80112929-6b65-4b9b-97bb-c9e2233f2ba2)
11) The data were then used in Umap to identify the proximity of the selected urban settlements:
![image](https://github.com/elenabolla/turin_crash_course-Elena/assets/167084001/c896f62f-cd10-4e3d-ad7a-4648dfa55d26)




