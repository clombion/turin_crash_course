# Project Proposal 

## Introduction
The phenomenon known as the Urban Heat Island (UHI) effect occurs when urban regions encounter higher temperatures in comparison to their surrounding locations and it is the result of dense populations of buildings, pavement, and other heat-absorbing surfaces that have replaced the natural land cover of an urban area. This effect raises air pollution levels, energy prices (for air conditioning, for example), the rates of heat-related illnesses and deaths, it raises risks of infrastructure damage and economic loss. Around the world, the urban heat island effect has an impact on numerous developing nations, especially those that went through rapid urbanisation and industrialisation without implementing adequate measure to mitigate its impact, such as India, Brazil, and Nigeria. The UHI effect poses great challenges for vulnerable populations, including urban homeless and migrants living in temporary camps who frequently lack access to shelter and adequate cooling facilities in cases of extreme heat. In this sense, data-driven solutions could be proposed and applied to enhance heat resilience, to empower vulnerable communities and improve their conditions.

## Project description and objectives
### Summary of goals
  This project aims to identify urban areas most affected by the urban heat island effect using weather and geospatial data, taking into considerations the presence of vulnerable people like the homeless and migrants. Moreover, the objective is to formulate feasible and data-driven approaches to implement heat-resilient solutions (such as shelters) and an information system to enhance the living circumstances for these vulnerable groups.
### Project Description
  The project aims to create a “Heat Risk Information System” with the purpose to provide information about the heat risks, peak of heat hours and locations for seeking shelter from the heat.
### Research question
  How can we effectively identify urban areas most affected by the urban heat island (UHI) effect, considering vulnerable populations and what heat-resilient solutions could we implement to enhance the living conditions of vulnerable groups? How can we develop an effective Heat Risk Information System to enhance the living circumstances of these vulnerable groups?
### Hypothesis
  Urban areas with high population density, particularly in developing regions are disproportionately affected by the urban heat island (UHI) effect. Implementing targeted heat-resilient solutions such as green infrastructure initiatives, heat-resilient shelter designs and developing a Heat Risk Information System will effectively mitigate the impact of the UHI effect and improve living conditions for vulnerable populations, including the homeless and migrants, in these areas.
### Objectives
  * Locate and chart regions where there is a high population density (especially considering the level of vulnerability) at risk of heat-related illnesses.
  * Implement heat-resilient solutions such as green infrastructures and heat-resilient shelter design to reduce the impact of the urban heat island effect. In particular, implement heat-resilient solutions that are feasible to the limited resources available in temporary refugee camps (prioritise solutions that are cost-effective, easy to implement, and adaptable to the camp's unique conditions).
  * Design and implement a Heat Risk Information System to provide real-time information about the risks, peak heat hours and locations for seeking shelter.
  * Provide education on heat safety through technologically based resources.
  * Evaluate the effectiveness of implemented solutions and the Heat Risk Information System in enhancing living circumstances for vulnerable populations and reducing heat-related health risks.

## Methodology
### Find
* Data sources: Geospatial and weather data ([NASA’s Worldview Earthdata](https://worldview.earthdata.nasa.gov/) and [SEDAC](https://sedac.ciesin.columbia.edu/downloads/maps/gpw-v4/gpw-v4-population-density-rev11/gpw-v4-population-density-rev11-global-2020.pdf), OECD database, OpenStreetMap, VisualCrossing)
* Contextual resources:
  * [UHI effect information](https://storymaps.arcgis.com/stories/e7edc8b871d94b418b16797b5782a30c)
  * Information on heat mitigation strategies ([link 1](https://earth.org/how-cities-around-the-world-are-tackling-the-urban-heat-crisis/), [link 2](https://www.meristemdesign.co.uk/blog/how-can-green-infrastructure-improve-air-quality-in-urban-areas) and [link 3](https://www.sciencedirect.com/science/article/abs/pii/S2210670722005844?fr=RR-2&ref=pdf_download&rr=87b6a3574e62bae8)).
### Get, Verify and Clean
* I have used NASA’s Worldview Earthdata to locate the main developing countries that are affected by the UHI effect using the population density filter.
* I have added the Land Surface Temperature filter to locate the areas with both high temperature and high population density. And I have selected 3/4 cities from Latin America, Africa and Asia. [Here](https://worldview.earthdata.nasa.gov/?v=-30.994288295002832,-21.549079180842686,171.07577826319687,70.80325592583452&i=2&l=Reference_Labels_15m(hidden),Reference_Features_15m(hidden),Coastlines_15m,MODIS_Terra_Land_Surface_Temp_Day,GPW_Population_Density_2020(opacity=0.79),BlueMarble_NextGeneration(hidden),VIIRS_NOAA20_CorrectedReflectance_TrueColor(hidden),VIIRS_SNPP_CorrectedReflectance_TrueColor(hidden),MODIS_Aqua_CorrectedReflectance_TrueColor(hidden),MODIS_Terra_CorrectedReflectance_TrueColor&lg=false&s=-46.6383,-23.5487%2B-58.3772,-34.6131%2B-77.0282,-12.0432%2B-70.5272,-33.3755%2B72.8212,18.969%2B76.4081,10.4501%2B77.2188,28.6324%2B3.3947,6.4541%2B36.82,-1.2858%2B28.2831,-15.4196&t=2023-05-15-T13%3A09%3A07Z) you can find the filtered map with the selected locations.
* I have used the [OECD](https://data-explorer.oecd.org/) website to retrieve data on population demography of vulnerable people living in specific locations by filtering the Historical population data with the countries of my interest.
* I have retrieved data on temperatures during specific months (I have selected the hottest months depending on the city) and download it as a CSV file and then merged the different CSVs into one using Excel. Then I used OpenRefine to tidy and clean the data I downloaded and filter to find the maximum temperature per each city (see [here](https://github.com/clombion/turin_crash_course/blob/WIP_Lucia/individual_folders/Lucia/Assignment/history_changes_weather_data.json) the history export). Then I have exported the cleaned data from OpenRefine and I have transformed it into a xls format [Link]() to the file. 
* Jupyther Notebook description ([link](https://github.com/clombion/turin_crash_course/blob/WIP_Lucia/individual_folders/Lucia/Assignment/Individual_assignment.ipynb) to the notebook):
  * Based on the areas that I have evidenced, I have used Nominatim Openstreetmap API to collect information on each city’s longitude and latitude
  * Once I have cleaned data on temperature using OpenRefine, I have added information about the highest temperature in a given country and I have added the information about vulnerable population demography.
* The file [RFP_Assignment3.csv](https://github.com/clombion/turin_crash_course/blob/WIP_Lucia/individual_folders/Lucia/Assignment/RFP_Assignment3.csv) contains a sum of the main data that I have collected, including name of the city and state, coordinates, maximum temperature and demographics of vulnerable populations.

## Proposed solutions
Some proposed solutions that aim to address the identified challenges related to urban heat islands and that are feasible to refugee camps and improve the living circumstances of vulnerable populations by providing access to cooling spaces, enhancing community resilience, and promoting data-driven decision-making and policy changes.
* **Implementing heat mitigation strategies**, such as planting trees and increasing green cover, creating shade structures and cooling stations, installing green or cool roofs and building heat resilient shelters.
* **Community engagement and outreach**: Launch community engagement and outreach programs to raise awareness about heat-related risks and available resources, including shelters and the Heat Risk Information System. Engage with local community leaders, NGOs, and relevant stakeholders to ensure that vulnerable populations are informed and have access to necessary support.
* **Heat Risk Information System**: Design and implement a user-friendly Heat Risk Information System that provides real-time information about heat risks, peak heat hours, and locations of nearby cooling spaces and shelters. The system should be accessible via mobile phones, websites, and other platforms commonly used by the target population.
* **Data-Driven Decision Making**: Use weather and geospatial data to inform decision-making processes related to urban planning and resource allocation. Analyze data trends to identify areas with the highest heat vulnerability and prioritize the implementation of heat-resilient solutions, including shelters and green infrastructure projects, in these areas.
* **Capacity Building and Training**: Provide training and capacity-building initiatives for relevant stakeholders, including urban planners, community organizers, and shelter staff, on heat-resilient design principles, heat-related health risks, and the use of the Heat Risk Information System. Empower local communities to take proactive measures to reduce heat-related vulnerabilities and enhance their resilience to extreme heat events.
* **Policy Recommendations**: Advocate for policy changes at the local and regional levels to integrate heat resilience into urban planning processes and address the needs of vulnerable populations. Propose policy measures such as heat action plans, zoning regulations for green spaces, and incentives for the development of heat-resilient infrastructure.

## Implementation plan
**Heat mitigation strategies**:
 * Make a list of all the resources—land, money, and supplies—that are available to support heat mitigation measures.
 * Select the locations: Identify priority locations for implementing heat mitigation strategies based on factors such as heat vulnerability, population density, and existing infrastructures.
 * Obtain the required supplies, machinery, and services by partnering with suppliers and contractors.
 * o	Engage with local communities, government agencies, NGOs, and relevant stakeholders to gather input, assess needs, and build partnerships for implementation.
**Community engagement and outreach**:
* Identify important stakeholders, neighbourhood associations, and vulnerable groups impacted by heat-related concerns by conducting a thorough needs assessment.
* List the community resources that are currently available and can work with outreach initiatives, such as neighbourhood NGOs, places of worship, community centres, and schools.
* To establish alliances and partnerships for community involvement, get in touch with representatives of the local government, non-profit organisations, and other pertinent parties.
* Create focused outreach programmes to interact with vulnerable communities, like the elderly, immigrants, and homeless persons.
**Heat Risk information system**:
* Conduct a needs assessment to find out what the target population needs and wants from the Heat Risk Information System
* To determine the most important features, usability preferences, and preferred communication routes, collect opinions via surveys, focus groups, and interviews.
* Collaborate with data scientists, software developers, and IT specialists to design and create the Heat Risk Information System.
* Based on user needs and industry best practices for information systems design, define the functionality, technical specifications, and requirements for the system.
* Define the functionality, technical specifications, and requirements for the system.
* To guarantee the system's reliability and rapidity, automate data gathering, analysis, and update activities.
* Provide an easy-to-use interface for the Heat Risk Information System that prioritises accessibility, clarity, and simplicity for a range of user types.
* Create a responsive online interface and mobile applications for iOS and Android smartphones to make the Heat Risk Information System available on a variety of platforms.
* Provide technical help and assistance to users who might run into issues or need more direction when using the system.
* Start an advertising campaign to educate the target audience about the advantages of the Heat Risk Information System. 
**Data-Driven Decision Making**:
* Determine which meteorological and geographic data sources—such as satellite images, land use maps, demographic information, and meteorological data—are pertinent.
* To get and compile the required datasets, enter into data-sharing agreements with governmental organisations, academic institutions, and other interested parties.
* Create procedures for gathering, processing, and storing data to guarantee accuracy, dependability, and adherence to data privacy laws.
* Engage with key stakeholders, such as citizens, community organisations, city planners, and government agencies, to exchange ideas, exchange findings, and jointly develop solutions based on insights from data.
**Capacity building and training**:
* Determine who should be involved in capacity building activities, such as community organisers, urban planners, shelter employees, and other community members.
* Conduct a needs assessment to determine particular knowledge gaps and training needs regarding heat-resilient design concepts, heat-related health concerns, and using the Heat Risk Information System
* Plan seminars, workshops, and training sessions to provide stakeholders with the capacity-building efforts. 
**Policy recommendations**:
* Examine current local and regional policies, rules, and urban planning frameworks in detail to determine how well they meet vulnerable populations' requirements and the goals of heat resilience.
* Determine the gaps, obstacles, and chances for incorporating heat resilience factors into frameworks for policy.
* Interact with important stakeholders such as legislators, public servants, urban planners, community leaders, and advocacy organisations to promote policy reforms and increase understanding of the value of heat resilience.
* Provide evidence-based policy suggestions that address the needs of vulnerable groups and include heat resilience into urban development procedures. 

## Conclusion
The issues faced by vulnerable populations in developing nations due to the urban heat island (UHI) effect are outlined in depth in this proposal. In particular, the problem of UHI affects migrants and the homeless in metropolitan areas who live in temporary shelters and do not have access to proper cooling facilities or shelter during periods of excessive heat. It also exacerbates already-existing environmental and health inequities. The primary goal of the project is to use targeted interventions and data-driven solutions to enhance public health and environmental resilience in metropolitan regions of developing nations. The combination of data-driven methods and useful interventions makes the solutions offered in this proposal both feasible and replicable. Vulnerable communities can better resist the difficulties of excessive heat by identifying metropolitan areas most affected by the UHI effect and implementing targeted heat-resilient solutions, such as green infrastructure efforts, heat-resilient shelter designs, and cooling facilities. 
Furthermore, the approach described in this proposal shows how to gather, analyse, and publish data in a methodical manner to support decision-making and direct the execution of heat resilience initiatives. Through the use of resources like NASA's SEDAC, Worldview Earthdata, and open-source software like Jupyter Notebook and OpenRefine, researchers may efficiently locate heat hotspots, evaluate their susceptibility, and create customised interventions for certain areas.
It is crucial to recognise this project's limitations, though. Accurately identifying susceptibility and executing customised interventions is hindered by the lack of data on the locations of refugee camps in developing nations and the effects of UHI in these areas. Furthermore, it is possible that some of the data used in this study are outdated, which could have an impact on how accurate the results are.
However, in spite of these limitations, the suggested research offers insightful analysis and establishes a foundation for solutions that may be modified and implemented in a variety of metropolitan environments and refugee camps across the globe. 
In conclusion, this research aims to pave the way for sustainable and replicable approaches to address the urban heat island effect, reduce heat-related health risks, and improve the well-being of vulnerable populations in both developing countries and temporary refugee camps by placing a priority on data-driven solutions, community engagement, and interdisciplinary collaboration.



