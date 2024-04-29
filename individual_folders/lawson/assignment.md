**Introduction**


As climate change continues to pose significant challenges, particularly in urban areas of developing countries, the Civic Literacy Initiative's commitment to enhancing environmental resilience and public health is commendable. With a keen focus on mitigating the adverse impacts of urban heat islands (UHI) on vulnerable populations, particularly the urban homeless and migrants living in temporary camps, your initiative embodies a crucial step towards fostering inclusive and sustainable urban development.
The intersection of urbanization, climate change, and social vulnerability underscores the urgency of addressing the disproportionate burden of extreme heat on marginalized communities. This Request for Proposals (RFP) presents a timely opportunity to harness innovation and data-driven approaches in identifying, analyzing, and mitigating the effects of UHI, thereby safeguarding the well-being of those most at risk.
In this response, we present a comprehensive proposal that leverages geospatial analysis, weather data, and community engagement strategies to develop actionable solutions aimed at reducing temperature disparities and enhancing resilience among vulnerable populations. By combining scientific rigor with a commitment to equity and social justice, our proposal seeks to empower communities and build capacity for sustainable adaptation to urban heat challenges.
Throughout this proposal, we underscore the importance of collaboration, recognizing that effective solutions require multi-sectoral partnerships and community-driven approaches. We look forward to the opportunity to contribute to the Civic Literacy Initiative's mission and collaborate towards creating more equitable and resilient urban environments for all.

**PROJECT DESCRIPTION**

The proposed project seeks to address the pressing challenge of extreme heat vulnerability in urban areas of developing countries, with a particular focus on the urban homeless and migrants living in temporary camps. By leveraging innovative data-driven approaches, community engagement strategies, and sustainable solutions, this project aims to mitigate the adverse effects of urban heat islands (UHI) and promote equitable access to safe and resilient urban environments.

**Research question**

How can geospatial analysis and community engagement strategies be effectively integrated to identify, prioritize, and address the unique heat vulnerability profiles of urban homeless and migrant populations in developing countries?

**Hypotheses**

Hypothesis 1:
Geospatial analysis can accurately identify hotspots of urban heat vulnerability among homeless and migrant populations in developing countries

Hypothesis 2:
Community engagement strategies, including participatory mapping and stakeholder consultations, enhance the effectiveness and sustainability of heat resilience interventions targeted at vulnerable urban populations.

Hypothesis 3:
Sustainable solutions developed in collaboration with vulnerable communities are more likely to be adopted, maintained, and scaled up, leading to greater resilience to urban heat islands and other climate-related risks.

**Hypothesis notes**

By overlaying weather data with demographic information on vulnerable populations, such as homeless shelters, migrant settlements, and low-income neighborhoods, it is possible to identify areas where these groups are most at risk of heat-related health impacts.

Identifying and mobilizing existing resources, such as community organizations, local government agencies, and non-profit groups, can help overcome barriers to implementation and ensure the sustainability of resilience initiatives.

**Actions** 
Here are the main proposed actions or steps needed to perform
Collect demographic data on vulnerable populations, including homeless shelters, migrant settlements, and low-income neighborhoods
Identify key stakeholders, including community organizations, local government agencies, and residents, for engagement.
Gather weather data from both forecast and historic sources for the target locations.
Collaborate with community members to co-design solutions and identify available resources in the area, such as green spaces, cooling centers, and community facilities.
Develop context-specific solutions to mitigate urban heat vulnerability, taking into account the findings from the data analysis and community engagement activities.
Establish monitoring and evaluation mechanisms to track the effectiveness and impact of resilience interventions over time
Collect data on key indicators, such as temperature reductions, heat-related health outcomes, and community engagement levels, to assess the success of the project.

**DATA COLLECTION Vulnerable populations in UHI context**

In this research, our aim was to identify and analyze vulnerable populations within the context of Urban Heat Islands (UHI). To streamline the process of collecting and organizing data, we utilized the online tool Smallpdf to convert a PDF document containing pertinent information into an Excel file. The source document can be found by clicking the following [link](http://kth.diva-portal.org/smash/record.jsf?dswid=-5921&pid=diva2%3A1820539&c=1&searchType=SIMPLE&language=en&query=Vulnerable+Populations+and+Urban+Heat+Islands%3A+A+Spatial+Analysis+of+Socio-Demographic+Factors+and+Heat+Exposure+in+Stockholm&af=%5B%5D&aq=%5B%5B%5D%5D&aq2=%5B%5B%5D%5D&aqe=%5B%5D&noOfRows=50&sortOrder=author_sort_asc&sortOrder2=title_sort_asc&onlyFullText=false&sf=all).
To extract and convert the data table from the PDF into a more easily manageable format, we used the Smallpdf tool.
Subsequently, upon obtaining the data in Excel format, we proceeded to convert it to CSV for storage and further analysis in our GitHub repository.

In [ ]: 
#Install to be able to convert from XLSX to CSV sudo apt-get install xlsx2csv     
In [ ]: 
#That copies the excel into the csv 
xlsx2csv UHIFile.xlsx --sheet 4 --delimiter ';' >> UHIFile.csv 

**Study outcomes **
The study shows that age is a critical factor in determining vulnerability to heat-related illnesses and mortality in urban heat islands (UHIs). Children under 5 and the elderly are particularly susceptible due to physiological factors like impaired thermoregulation.

Income level is also an important consideration, as low-income communities tend to be located in areas with less greenery and more artificial surfaces, leading to higher temperatures. Low-income individuals also have less access to cooling equipment and healthcare services.

The study utilizes temperature data from satellite imagery collected by the Swedish Civil Contingencies Agency, which provides high-resolution (30m) heat maps covering the study area from 2017-2022.

Socio-demographic data on factors like age, income, ethnicity, education, and residential type was collected from Statistics Sweden at the DeSO (small statistical area) level to analyze the vulnerability of different population groups to UHI effects.

In summary, the key outcomes relate to identifying the most vulnerable population groups to heat-related health impacts in the Stockholm region, based on both physiological and socioeconomic factors, and utilizing detailed temperature and demographic data to spatially analyze these vulnerabilities.


**Case of Study **
For the RFP, we will prioritize Stockholm, situated in Sweden, a nation in Northern Europe. Our concentrated efforts in Stockholm are aimed at devising a methodology for data collection, analysis, and proposing solutions that can be readily extended and duplicated in other regions.
Country : Sweden

Study type: Cross-sectional 

Findings : Population density is relatively low compared to many other European countries, with a population of around 10.5 million people as of 2021. However, population density can vary significantly across different regions of Sweden, with urban areas such as Stockholm, Gothenburg, and Malmö having higher population densities compared to rural areas.
population density is indeed associated with the level of heat stress experienced by residents in urban areas. Higher population densities can lead to more significant heat retention and reduced airflow, exacerbating the UHI effect and increasing the risk of heat-related illnesses such as heat exhaustion and heatstroke. Vulnerable populations, such as the elderly, children, and individuals with pre-existing health conditions, may be particularly susceptible to the effects of heat stress in densely populated urban areas.


Stockholm, the capital city of Sweden, falls under the Köppen climate classification system as having a humid continental climate (Dfb). This classification indicates warm to hot summers and cold winters, with precipitation spread relatively evenly throughout the year. However, Stockholm's location on the eastern coast of Sweden moderates its climate somewhat compared to inland areas, with milder winters and cooler summers than areas farther inland.
Summers in Stockholm are generally warm, with average high temperatures ranging from 20°C to 25°C (68°F to 77°F). However, occasional heatwaves can push temperatures higher. Summer is the driest season, but rainfall can still occur, typically in the form of short thunderstorms.
Autumn brings cooler temperatures, with average highs decreasing from around 15°C (59°F) in September to 5°C (41°F) in November. Rainfall increases during this season, and cloudy days become more common.

Winters in Stockholm are cold and snowy. Average high temperatures range from around 0°C to -3°C (32°F to 27°F), and temperatures can drop below freezing frequently. Snowfall is common, especially from December to February, with the city often covered in a blanket of snow.

Spring is a transitional season, with temperatures gradually warming up. Average highs climb from around 5°C (41°F) in March to 15°C (59°F) in May. Snowfall becomes less frequent, but rain showers are common, especially in April and May.


THE IMPACTS OF LAND COVER TYPES ON AMBIENT TEMPERATURES IN STOCKHOLM
The impacts of land cover types on ambient temperatures are influenced by various factors:
Urban Heat Island Effect: Urban areas typically experience higher temperatures than surrounding rural areas due to the urban heat island (UHI) effect. The UHI effect is caused by human activities such as the construction of buildings and roads, which absorb and retain heat, as well as the reduced presence of vegetation compared to rural areas. In Stockholm, densely built-up areas with more buildings and infrastructure tend to have higher temperatures than less developed or vegetated areas.
Vegetation and Green Spaces: Green spaces such as parks, forests, and gardens play a crucial role in mitigating the UHI effect by providing shade and evaporative cooling. Areas with abundant vegetation tend to be cooler than built-up areas because plants release moisture through transpiration, which cools the surrounding air. In Stockholm, neighborhoods with more trees, parks, and green spaces can experience lower ambient temperatures compared to areas with less vegetation.
Water Bodies: Water bodies, such as lakes, rivers, and coastal areas, can moderate temperatures in urban areas by absorbing heat during the day and releasing it slowly at night. In Stockholm, the presence of water bodies like Lake Mälaren and the Baltic Sea can influence local temperatures, especially in areas close to the waterfront.
Building Materials and Urban Design: The materials used in buildings and urban infrastructure can affect local temperatures. Materials like concrete and asphalt tend to absorb and retain heat, contributing to higher temperatures in urban areas. Conversely, lighter-colored or reflective surfaces can help reduce heat absorption and lower ambient temperatures. Additionally, urban design factors such as street orientation and building density can influence airflow and the distribution of heat within the city.
Land Use Patterns: The distribution of land use types, such as residential, commercial, industrial, and recreational areas, can also influence ambient temperatures. Industrial areas with extensive pavement and infrastructure may experience higher temperatures, while residential neighborhoods with more green spaces and lower building density may be cooler.


**Land Surface Temperature (LST)**
Land Surface Temperature (LST) refers to the radiant heat emitted by the Earth's surface, as observed from space. It essentially represents how warm the Earth's surface would feel if touched at a specific location. When viewed from a satellite, the Earth's surface is whatever is visible through the atmosphere, whether it's snow, grass, rooftops, or forest canopies. It's important to note that LST differs from the air temperature reported in weather forecasts.
To access Land Surface Temperature (LST) data for Stockholm , one can utilize sources like [Glovis](https://glovis.usgs.gov/app) (Global Visualization Viewer), which provide satellite imagery datasets. 
Specifically, the Moderate Resolution Imaging Spectroradiometer [(MODIS)](https://modis.gsfc.nasa.gov/) satellite's LST data is employed to gauge the Urban Heat Island (UHI) effect in theSweden.
In light of this, one can gather relevant information from these sources by referring to guide documents such as:
MODIS Land-Surface Temperature Algorithm Theoretical Basis Document [(LST ATBD )](https://modis.gsfc.nasa.gov/data/atbd/atbd_mod11.pdf)
[MODIS Land Surface Temperature Products Users' Guide](https://www.icess.ucsb.edu/modis/LstUsrGuide/MODIS_LST_products_Users_guide.pdf) 
Following these guidelines, individuals can learn [How to download LST information from Modis typically accessed through the MODIS](https://www.icess.ucsb.edu/modis/LstUsrGuide/usrguide.html) data pool [link](https://lpdaac.usgs.gov/tools/data-pool/) . 
This process allows for the retrieval of comprehensive information regarding Land Surface Temperature, aiding in studies related to urban heat islands and environmental monitoring in Stockholm.


**MOD11A1 product** 

The MOD11A1 product, derived from observations by NASA's Terra satellite's Moderate Resolution Imaging Spectroradiometer (MODIS) instrument, furnishes daily global Land Surface Temperature (LST) data. MOD11A1 product images data can be found here link
MODIS products can be found in this [link](https://e4ftl01.cr.usgs.gov/MOLT/)
This dataset offers insights into the surface temperature of Earth's land areas at a spatial resolution of 1 kilometer. It is available in either an integerized sinusoidal or sinusoidal projection format. Each MOD11A1 product comprises a grid of 1200 rows by 1200 columns, covering the entirety of the globe. This product serves as a snapshot of land surface temperature for a single day, facilitating daily monitoring and analysis of temperature fluctuations on Earth's surface.


To visualize and analyze the data effectively, a tool like HDFView could be necessary. HDFView is a free visualization tool that enables you to open and explore all HDF files. Utilizing this tool, we can generate the final report using geospatial information on land temperature and identify Urban Heat Islands (UHIs) within the desired area.


RELATIONSHIP BETWEEN AMBIENT TEMPERATURES AND VULNERABLE POPULATIONS 
Population density allows us to correlate with the retrieved Land Surface Temperature (LST) information and pinpoint Urban Heat Islands (UHIs) where vulnerable populations may be affected. This understanding can aid in devising potential solutions. To access population density information, we can utilize the resources available on the [Worldpop HUB page](https://hub.worldpop.org/geodata/listing?id=69). This platform offers various data sources that can support our investigation into demographic patterns and behaviors.

**RELATIONSHIP BETWEEN AMBIENTTEMPERATURES AND VULNERABLE POPULATIONS** 


If we narrow down our search to the Sweden, we can access map data spanning the last 20 years and download it. For instance, we could download data from the year 2020. However, due to its size exceeding 25MB, the file cannot be uploaded to the GitHub folder. Nonetheless, it can be downloaded from the provided  [link](https://hub.worldpop.org/geodata/summary?id=28283) if necessary. 


**Identify specific locations with high temperatures and high percentages of vulnerable population** 

To pinpoint specific areas with both high temperatures and high percentages of vulnerable populations, we turn to various sources of data. 
Research indicates that around one-third of Stokholm residents live in informal settlements characterized by inadequate housing and infrastructure, which are exacerbated by poverty and urbanization trends. An analysis of the exposure layer output illustrates that densely populated regions coincide with elevated Urban Heat Island (UHI) values. Consequently, a considerable portion of the population is exposed to the amplified temperatures associated with UHI effects.
Furthermore, considering the vulnerability of older individuals to extreme temperatures due to existing illnesses and decreased tolerance, we focus on identifying the locations where people aged 60 to 80 typically reside. This demographic information is extracted from the [Worldpop HUB](https://hub.worldpop.org/geodata/summary?id=50543), focusing on the specified age range. The data, previously downloadable and convertible from TIF to PNG format, provides valuable insights.
All related images can be accessed in the provided "Following folder.“
By integrating data from both sources, we can estimate and assess which UHI-affected areas disproportionately impact vulnerable populations. This facilitates the creation of a prioritized ranking of areas for initiating assessments and planning interventions based on the geospatial information gathered.


**SOLUTION DEVELOPMENT** 

The conventional strategies to combat Urban Heat Islands (UHIs) across different neighborhoods and communities typically include:
Enhancing Greenery: This involves planting trees and fostering vegetation growth in urban areas to mitigate UHI effects, enhance air quality, and offer shade and cooling benefits to residents.
Implementing Green or Cool Roofs: Installation of green or cool roofs on buildings aids in reducing heat absorption. Green roofs entail vegetation growth, while cool roofs utilize materials that reflect sunlight and heat.
Exploring Cool Pavement Solutions: Innovative pavement solutions like cool pavements, which reflect more solar energy and enhance water evaporation, help lower surface temperatures and enhance nighttime visibility. More information 
Adopting Smart Growth Principles: Consideration of smart growth principles in urban planning, focusing on creating compact, walkable communities with diverse land uses, efficient transportation options, and preserved open spaces, promoting sustainable development and resilience to climate change impacts.
However, when addressing low-income neighborhoods or areas with limited resources, adjustments are necessary. Here are modified proposals:
Affordable Solutions: Implementing low-cost solutions using locally available materials, such as community-led tree planting initiatives using indigenous species.
Utilizing Light Colors: Employing light-colored materials or painting surfaces white to reflect sunlight and reduce heat absorption, particularly effective on roofs, pavements, and walls to lower temperatures.
Capacity Building: Investment in education and training programs focusing on design, installation, and maintenance, empowering local communities and fostering ownership of sustainable development projects.
Building Partnerships: Collaborating with local governments, NGOs, community organizations, and international development agencies to leverage resources, expertise, and funding.
Adaptation and Innovation: Customizing green infrastructure solutions to suit specific community needs and environmental conditions, utilizing innovative approaches like vertical gardens or green walls to maximize limited space and enhance cooling benefits and air quality.
Promoting Community Engagement: Encouraging community participation through inclusive decision-making processes and consultations, empowering local communities and ensuring ownership of sustainable projects.


**HERE'S A SUMMARIZED LIST OF TOOLS AND METHODS UTILIZED**


Data Collection and Organization: 
Used Smallpdf to convert PDF documents to Excel for data extraction.
Converted Excel files to CSV format for better storage and analysis.
Meteorological Data Retrieval:
Retrieved meteorological data from the Sweden’s weather bureau.
Utilized MODIS satellite data and Glovis for Land Surface Temperature (LST) information.
Image Processing and Visualization:
Converted TIF image files to PNG format for improved visualization.
Employed HDFView for exploring and visualizing HDF files containing temperature data.
Population Density Analysis:
Accessed population density data from Worldpop HUB.
Analyzed and visualized demographic data to understand population distribution.
Proposal Development:
Created mitigation strategies for addressing Urban Heat Islands (UHIs).
Adapted standard strategies for low-income neighborhoods or areas with limited resources.
Implementation Planning:
- Identified necessary steps, resources, and partnerships for implementing proposed solutions.





















