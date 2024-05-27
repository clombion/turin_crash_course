# Request for Proposals (RFP):Mitigating Urban Heat Islands for Vulnerable Populations in Developing Countries

# A Case Study of Nairobi - Kenya
**by:**
**Christian Serge BASHIGE**
1138451 - BSHCRS84A23Z312E

![Alt Naistud01](https://github.com/clombion/turin_crash_course/assets/166433063/12675937-81d4-46b9-9165-856246835b66)

#  Master ICT for Development and Social Good
  **UNIVERSITY OF TURIN** 
  
#  Crash Course #1: Data in-practice, final assignment 
**April 28th 2024**

# Professor: 

# Cedric Lombion

## ABSTRACT

In this assignment the Urban Heat Island effect is investigated and the effect of urbanization on UHI is
analyzed as a case study in Nairobi City. The primary aim of this study was to provide a
comprehensive quantification of the effect of Urbanization to the UHI effect to the urban
planning management. The study consisted of three parts; Analysis of Urbanization using the
DMSP/OLS nighttime light images, investigation of UHI effect using Landsat 8 OLI/TIRS
images and correlation analysis between the UHI, NDVI (representing vegetated surfaces) and
Urbanization(landuse/Landcover) to establish a relationship between the UHI effect and
urbanization. A mono-window algorithm was used to retrieve the land surface temperature (LST)
distribution from the Landsat 8 images, using specifically band 10 and band 11 images. The
spatial pattern of LST in the study area retrieved to characterize their local effects on the urban
heat islands. In addition, the correlation between LST and the NDVI (Normalized difference
vegetation index), Urbanization was analyzed to explore the impacts of the vegetation and
urbanization on the urban heat island effect. The results indicate that, though not pronounced,
there is a distribution of heat islands in Nairobi. The negative correlation between LST and
NDVI suggests that vegetation weakens the heat island effect, while the positive correlation
between LST and Urbanization indicates that the urbanization elevates the heat island effect. The
study concluded that, with the rate of urbanization, the distributed heat island, with time will
conglomerate into a large heat island in the region. Although satellite data (e.g., Landsat 8 level
one products) can be applied effectively to examine the distribution of urban heat islands, the
research still needs to be refined with in situ measurements of LST in future studies.
![Alt Naistud0](https://github.com/clombion/turin_crash_course/assets/166433063/1d3c303d-1062-4297-b375-f18dcd83f238)

Figure 1Urban heat island formation 
Source:https://www.insightsonindia.com
# Keywords
**Urban Heat Island**, **Mitigation**, **Adaptation**, **Dynamic Modelling**, **Urban Planning**

# Table of contents
# 1.	Abstract

# 2.	Introduction
2.1.	Study on Urban Heat Island - Project Description
2.2.	Mitigation of Urban Heat Island

# 3.	Method, Tools, and Information
    3.1. Increasing, Characterization and Analysis of Urban Space
    3.2. Building of Mitigation-Adaptation Scenarios

# 4.	Results and Actions
    4.1. Urban Planning, Mitigation and Adaptation to the UHI
     4.2. Inclusion of the Results into the Planning Process

# 5.	Conclusion

# List of Abbreviations and Acronyms

**UHI** - Urban Heat Island
**UBL** - Urban Boundary Layer
**UCL** - Urban Canopy Layer
**LST** - Land Surface Temperature
**LSE** - Land Surface Emissivity
**NDVI** - Normalized Difference Vegetation Index
**TM** - Thematic Mapper
**ETM+** - Enhanced Thematic Mapper plus
**OLI** - Operational Land Imager
**TIRS** - Thermal Infrared Sensor
**SNR** - Signal to Noise Radiometric
**WGS** - World Geodetic System
**UNESCO** - United Nations Educational, Scientific and Cultural Organization
**EIA** - Environmental Impact Assessments
**EPA** - Environmental Protection Agency
**KMD** - Kenya Meteorological Department
**CBD** - Central Business District
**USGS** - United States Geological Survey
**RGB** - Red, Green, Blue Band layers
**DMSP/OLS** - Defense Meteorological Satellite Program - Operational Linescan System
**DN** - Digital Number
**GIS** - Geographic Information System 

## 1.1	INTRODUCTION AND STUDY AREA

## 1.2	Introduction
In Nairobi City, infill development and urban sprawl are leading to the loss of vegetation and the ratio of land use have increased over the years, these are majorly composed of impervious surfaces such as buildings and parking areas and tarmac roads as well. This therefore has affected the heat balance provided by the natural ecosystem. As warming associated with urban development and climate change intensifies, vulnerable groups will be at risk of heat- related morbidity and mortality. This warming of the city due to the related urbanization and other factors has led to Urban Heat Island effect. The UHI effect is a critical factor for air quality management and public health in urbanized areas all over the world. This effect is relating to an increase in temperatures in urban areas as compared to the surrounding lower density rural areas.
## 1.3	Study Area
The study area is Nairobi, which is the largest city in Kenya and the country’s capital with a focus on the densely urbanized and populated areas. The main focus is the Nairobi which is considered fully urbanized with most surfaces covered with tarmac or various construction materials such as buildings and parking lots. There is maximum land use with minimum vegetation cover compared to the surrounding and during the day and various nights the area is highly populated as much of the activities are carried out in the city Centre. This therefore makes it an ideal area of study for the research topic. It lies in between the latitude 1016’59” South; Longitude 36°49’00’’ East, with an elevation of 1684m above the sea level according to WGS 84 (Latest World Geodetic System) (figure 1.2) 
![Alt Naistud1](https://github.com/clombion/turin_crash_course/assets/166433063/8151356b-ea83-44e0-b12c-65d041d4b9df)
## Figure 1.2 (source: drawn with ArcGIS 10.3): the map showing Nairobi region, study area
![Alt Naistud2](https://github.com/clombion/turin_crash_course/assets/166433063/88164ad2-be1f-41df-8031-b1ffde2225b3)
## Figure 1.3 :( source: Google maps): showing the Nairobi, focused study area. 

# 1.3.1. Study on Urban Heat Island - Project Description

Soon it is expected that the global rate of urbanization will increase by 70% of the present world urban population by 2030. As urban agglomerations emerge and population migration from rural to urban/suburban areas continues, sustainable urban planning faces two major challenges: first the impact of climate change and the necessity for adaptation measures to mitigate the consequences, and second, that of urbanization and the necessity of balancing the various conflicting spatial demands. For to address these issues a comprehensive study on some of the effects related to urbanization is necessary.
Urbanization negatively impacts the environment mainly by the production of pollution, the modification of the physical and chemical properties of the atmosphere and covering of the land surface. Considered to be a cumulative effect of all these impacts is the UHI effect, defined as the rise in temperature in any man-made area, resulting in a well- defined, distinct “warm Island” among “Cool Sea” represented by the lower temperatures during the day and then re-radiate it at night (Quattro chi et al 200; Oke 1982)) (figure 1.1).
![Alt Naistud3](https://github.com/clombion/turin_crash_course/assets/166433063/ab1a8506-8912-48a8-b3cb-cc42c53ba377)
## Figure 1.1(source; EPA, 2008): Sketch of an Urban Heat Island Temperature Profile for late afternoon.
The UHI effect is a worldwide concern; in Europe, climate change projections suggest that the summer heat waves will become more frequent and severe during this century, consistent with the observed trend of the past decades [1]. This will also be true for the Northwest Europe, including the Netherlands [2]. While urban areas will generally be exposed to the same change in regional climate as the surrounding areas, the urban setting can exacerbate the impact of this exposure on a local scale, this is influenced by the fact that urbanization will continue in the next decade at a higher rate. These developments may significantly influence future urban climate conditions, thermal comfort of citizens and livability of urban areas.
The presence of many buildings and artificial or impervious surfaces at the expense of the natural environment, creates a unique local climate altering temperature, moisture, wind
patterns and radiation. 

# 2.3 Mitigation of Urban Heat Island

It is well-known and documented that urbanization can have significant effects on local weather and climate [1]. UHI as an effect of urbanization is the direct representation of environment degradation [3]. The high urbanized areas lead to more distinct urban heat island with huge temperature differences between urban and rural areas. As early as1833, the concept of UHI was described by Luke Howard [4]. The buildings, concrete, asphalt, and industrial activities of urban areas causes the UHI effect. UHI mainly appeared in the spatial distribution of land surface temperature (LST), which is governed by heat fluxes and affected by urbanization. Consequently, acquiring LST is the primary and key step to the UHI analysis. 

# UHI - Problem Statement

Urbanization is slowing down wind speed as buildings and other structures block the flow path, as a result, pollutants are not being properly dispersed putting the health of hundreds of thousands of city residents at risk. Recent studies show that Nairobi is on a risky path of becoming a large heat island as tall skyscrapers block the dispersal of pollutants (June 2015 UNESCO conference “Our Common Future Under Climate Change”). This therefore shows that the situation of urban heat Island has not been established with the recent studies done. This therefore creates a study area leading to this investigation. The UHI effect, together with solar radiation set in motion conditions that that foster biophysical hazards such as heat stress and increased concentration of secondary pollutants.

# UHI - Justification

The Kenya economic survey indicate that the effects of climate change continue to be felt in Kenya in the form of high temperatures and droughts. It also reports that total number of environment impact assessment risks increased by 35.6% from 1153 in 2013 to 1563 and, that human settlements and infrastructure sector accounted for the highest number of EIAs reported over the years followed by the transport sector. This therefore shows that urbanization influences the temperatures variations especially in Nairobi. Although UHI effect studies has been done in the major developed countries, in Africa continent there is reported few studies conducted making a need for such studies in order to inform city planners to cope with the challenges of urban climates.
# RFP Tools Objectives
The study hypothesized that the population increase associated with urbanization will lead to modification on the urban local weather hence the effect of UHI. The study aims at evaluating the temporal patterns of urbanization and investigation of urbanization effects on the temperature, which will be vital in enhancing human comfort as well as ensuring environmental sustainability.
# The main objectives of this project are:
## 1.	To contribute to the effective environmental management of Nairobi on the effect of UHI and population growth.
## 2.	The analysis of the UHI effect on vulnerable population using satellite images
## 3.	Analysis of Urbanization
# The specific tools will serve to:
## 1.	Downloading Landsat images.
## 2.	Correction of the images 
##  3.	Analysis of the UHI using Geo Localization
## 4.	Downloading nighttime light images 
## 5.	Analysis of urbanization and classification of the images
## 6.	Establishing a relationship between the UHI effect and Urbanization. 

![Alt Naistud4](https://github.com/clombion/turin_crash_course/assets/166433063/7dd8c14e-f52f-4df6-925f-07d626d06f21)
Figure 2.1: (source; EPA) showing the magnitude of the urban heat island as a temperature difference between a city and its surroundings, for clear sky and light wind.

![Alt Naistud5](https://github.com/clombion/turin_crash_course/assets/166433063/f405f530-daef-44f8-8874-510caf654b1c)
Figure 2.2: (source; Daily Nation (online)) showing trapped pollutants over Nairobi CBD.

# 2.1.1	Urban Heat Island-Types
Broadly, according to (Oke, 1987), there are three different types of urban heat island defined as follows:
*i.	Canopy layer or air UHI- this includes urban canopy layer heat island that is found in the air beneath the roof level and the urban boundary layer heat island that is found in the air above the roof level. These are closely coupled but have different magnitudes and are generated by different processes.**
*ii.	Boundary layer (UBL) heat island or surface UHI. This kind can be distinguished based on the temperatures of urban surfaces.
*iii.	Subsurface urban heat island- is that which is associated with the ground beneath the surface.

# 3.1	DATA AND METHODOLOGY
## 3.1.1	Data
Landsat 8 O was used in the retrieval of land surface temperature due to the presence of thermal infrared bands. The Nighttime light images were used in analysis and classification of urbanization, these products are widely used in urban studies and energy or population research (Table 3.1)
# Table 3.1 Landsat and Nighttime Light images
## Data|Resolution (m)|Time|Date
------|--------------|----------
Landsat8|30x30|Day and night time|2013-2014
------|-------|------|-----------
Nighttime Light Earthdata|120x120|Night Time|2013-2014

# 3.1.1.1	Other Auxiliary Data
In addition, the GIS boundary data for Kenyan Districts, the Landuse/Landcover TIFF format data were downloaded from the ILRI website to help in the analysis as well. And Geosojon file was generated that contain all the soil information
# 3.1.2.1	Urbanization investigation
DMSP/OLS products are widely used in urban studies. One of the most frequently used data from DMSP/OLS is the version 4 of global nighttime light series, which provide annual global composite imagery.
After collecting the image from we have uploaded them to our GitHub repository using the method below:
**![Alt text](images/example.png)**
And
	
**![Alt text](https://example.com/path/to/image.png)**
The soil data collected from varda plateforme SoilHive iin  csv format that we converted into xls file then imported into PowerBi for Analyzing, cleaning and dashboard report

# 3.1.2.2. Vulnerable population in urban heat island Nairobi

Vulnerable populations encompass a diverse range of individuals, including low-income communities, the elderly, children, and others with limited resources or specific vulnerabilities. These groups face unique challenges when it comes to coping with the intensified heat in urban areas, making it imperative to explore the negative aspects of urban heat’s impact on their lives.

**Increased Risk of Heat-Related Illnesses:** Urban heat creates a hazardous environment, particularly during heatwaves. The elevated temperatures can lead to a surge in heat-related illnesses, including heat exhaustion and heatstroke. Vulnerable populations, such as the elderly and those with pre-existing health conditions, face heightened risks. The negative effects on human health can be severe, sometimes even fatal.
**Impact on Vulnerable Groups:** Vulnerable groups within urban areas are disproportionately affected by the health risks posed by urban heat. Elderly individuals, who often have reduced heat tolerance and limited mobility, find themselves at greater risk. Similarly, children are more susceptible to heat-related illnesses, and the inability to access air conditioning in many low-income neighborhoods exacerbates their vulnerability.
Urban heat doesn’t discriminate, but its effects are disproportionately felt by certain segments of the population. In this section, we delve into the specific vulnerabilities of different groups and examine how urban heat impacts their daily lives.

# Low-Income Communities

**1.	Lack of Access to Air Conditioning:** For many low-income households in Nairobi areas, access to air conditioning is a luxury they cannot afford. This lack of access means that during extreme heat events, Nairobi residents must endure dangerously high indoor temperatures, putting their health and well-being at risk. As a negative consequence, energy bills can skyrocket when individuals do use air conditioning, leading to financial strain.
**2.	Limited Green Spaces:** Low-income neighborhoods often lack green spaces and tree cover, which can act as natural coolants. The absence of parks and greenery leaves residents with fewer options for seeking refuge from the heat. These communities are disproportionately exposed to the urban heat island effect, exacerbating the challenges they face during heatwaves.

# Elderly Population

## *1.	Health Risks Due to Reduced Heat Tolerance The elderly are particularly vulnerable to the negative impacts of urban heat due to reduced heat tolerance. As people age, their bodies become less efficient at regulating temperature, making them more susceptible to heat-related illnesses such as heat exhaustion and heatstroke. The lack of climate-controlled environments can pose serious risks to their well-being.*
## *2. Social Isolation During Heatwaves During extreme heat events, elderly individuals may be reluctant to leave their homes, leading to social isolation. This isolation can have adverse effects on mental and physical health. Connecting with support systems becomes challenging when venturing outside is uncomfortable or even dangerous.*

# Children and Schools

**1.	Impact on Learning Environments:** Schools are not immune to the effects of urban heat. Increased temperatures can create uncomfortable and distracting learning environments for students. Concentrating on studies becomes difficult when classrooms lack proper cooling, impacting the educational experiences of children.
**2.	Heat-Related School Closures:** In some cases, extreme heat can lead to the closure of schools, disrupting the routines of both students and parents. Such closures can result in lost instructional time and place an additional burden on parents who may need to arrange for alternative childcare during these closures.
**3.	Children and Babies:** Children and babies are especially vulnerable to heat due to being unable to effectively protect themselves from the heat without assistance. From a combination of physiological factors, limited coping mechanisms, and their inability to effectively protect themselves from extreme heat.
Understanding how urban heat uniquely affects these vulnerable populations is essential for crafting targeted interventions and policies aimed at mitigating the disparities in heat-related risks and impacts. In the following sections, we will explore strategies and initiatives that can help alleviate these challenges and create more equitable and resilient urban environments.

# UHI and environmental consequences 

**Stress on Urban Ecosystems:** Urban heat exacerbates the stress on already fragile urban ecosystems. Elevated temperatures can damage vegetation and urban green spaces, leading to reduced biodiversity and aesthetic degradation. These effects undermine the capacity of cities to provide green areas for recreation and to mitigate the urban heat island effect.
**Aggravation of Air Pollution:** Urban heat exacerbates another urban challenge: air pollution. Higher temperatures can increase the formation of ground-level ozone, a major component of smog, and can intensify the emissions of pollutants from vehicles and industrial sources. This combination of heat and pollution further deteriorates air quality, posing serious health risks to urban residents.
Understanding the negative consequences of urban heat is essential to formulating effective strategies for mitigating its impact on vulnerable populations. As we proceed, we will explore how these challenges can be addressed through various initiatives and interventions at both the community and policy levels. The analysis was carried out step by step (figure 3.1)
![Alt Naistud6](https://github.com/clombion/turin_crash_course/assets/166433063/081457a2-4b88-44c7-b7ef-b2aa350c2030)
Figure 3.1: flow chart showing the process of Urbanization analysis.

# Conclusion And Recommendations
## 5.1.1	Conclusion
In this study, the mono-window algorithm was applied to retrieve the LST in Nairobi using the Landsat 8 OLI/TIRS level one product data. Through the retrieved temperature data, it I found that the distribution of UHI in Nairobi is mainly located in residential areas and maximum at the city Centre. It is noticed that with the urbanization growth rate, soon, the distributed heat islands will conglomerate into one large-scale regional heat Island. In comparison, the scattered urbanized areas have dispersed distribution of urban heat island effects, it is therefore reasonable to envisage the establishment of satellite-urban areas in the city layout separate from the business center to prevent the formation of a large-scale regional urban heat island.
In the absence of non-uniform distribution of ground weather stations, remotely sensed data have a great importance to monitor impacts of different environmental issue such as heat islands. The thermal band in the Landsat satellites, have been proven to have a crucial role in estimating surface temperatures. The availability of different algorithms developed by different authors to overcome the shortage of data required for calibrating the satellite estimated surface temperature to field of study made the study be conclusive with minimal errors per see. The mono-window algorithm developed by Qin Z and Berliner is one of these algorithms that have a great importance in case of missing in situ data of ground emissivity; atmospheric transmittance and mean atmospheric air temperature.

# The obtained results from this study are concluded as follows.

## **•	UHI exists throughout the year, regardless of the season i.e. warm or cold seasons in the two investigated dates.* 
## **•	The two types of heat islands, the surface and the urban, exists in the study area though not very pronounced compared to other cities of the developed nations.* 
##  **•	The value of Urban heat island over the urban area is ranging from 0.5 to 3.5°C above the mean temperatures of the urban areas and it is much related to the existing land use/Landcover.*
## **•	UHI which was the main concern in this PROJECT is much related to the urbanization.*

# 5.1.2	Recommendations

A recommendation to the urban planners is to consider the scattered plan of urban areas, to distribute the heat Island to minimize the UH becoming one large heat island in the region, they are also to consider the material used in the building structures to enable mitigate the UHI effect or its further generation.
Detailed research that considers the parameters such as humidity, wind speed, analysis of the production of anthropogenic heat, analysis of materials used in the building structures, in situ meteorological data of the time that the satellite passed the study area. To be able to quantify the UHI effect is recommended. This is so because the analysis in this report only focused on the distribution and the difference of the LST. 

# 5.1.3. How do we Reduce the Urban Heat Island? Positive Strategies

Reducing the impact of urban heat is a multipronged approach with the potential to enhance urban livability, improve public health, mitigate climate change, and foster greater resilience in our cities.
Increasing the number of parks, green roofs, and urban vegetation can significantly reduce the UHI effect. Trees and plants provide shade and release moisture through a process called transpiration, which cools the surrounding air. This helps create a more comfortable microclimate and reduces the heat absorbed by concrete and asphalt surfaces.
Positive 2: Enhanced Aesthetics and Quality of Life
Expanding green spaces not only mitigates the UHI but also enhances the aesthetics and quality of life in urban areas. Parks and greenery provide recreational opportunities, improve air quality, and create more pleasant and inviting environments for residents and visitors.
The increased planting of trees in urban areas are a key warrior in the fight against urban heat. Trees Provide a wide range of environmental, medical, and social benefits to their surroundings.

# Positive Strategy 2: Cool Roof Initiatives and Reflective Surfaces

## Positive 1: Reduced Heat Absorption

Cool roof initiatives involve using reflective materials or coatings on roofs to reduce heat absorption. These roofs reflect more sunlight and absorb less heat, helping to lower temperatures in urban areas. This can be particularly effective in reducing indoor temperatures and energy consumption in buildings.

## Positive 2: Energy Efficiency and Cost Savings

Cool roofs can lead to significant energy savings by reducing the need for air conditioning during hot weather. This not only lowers electricity bills for building owners but also decreases the overall energy demand in cities, contributing to sustainability goals and reducing greenhouse gas emissions

![Alt Naistud7](https://github.com/clombion/turin_crash_course/assets/166433063/5ac9101a-a2d4-4d85-afbd-e47a93b691ec)
Fig 4. Image of comparison City with deforestation and city with trees planting 

# 5.1.3	References
[1]	Kenya National Bureau of Statistics http://www.knbs.or.ke/.
[2]	National Geophysical Data Center. http://ngdc.noaa.gov/eog/.
[3]	City Green https://citygreen.com/how-to-lower-urban-heat-with-tree-canopy/  






 

