# URBAN HEAT ISLAND (UHI): Request for Proposals (RFP): Mitigating Urban Heat Islands for Vulnerable Populations in Developing Countries
# A Case Study of Nairobi - Kenya.
*by
Christian Serge BASHIGE
1138451 - BSHCRS84A23Z312E
# Master ICT for Development and Social Good
# UNIVERSITY OF TURIN

# Crash Course #1: Data in-practice, final assignment 
*April 28th 2


Professor:  Cedric Lombion

**ABSTRACT**

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
Figure 1Urban heat island formation 
Source:https://www.insightsonindia.com
# Keywords
Urban Heat Island, Mitigation, Adaptation, Dynamic Modelling, Urban Planning

## Table of contents
** 1.	Abstract
** 2.	Introduction
 * 2.1.	Study on Urban Heat Island - Project Description
 * 2.2.	Mitigation of Urban Heat Island

** 3.	Method, Tools, and Information
  *3.1. Increasing, Characterization and Analysis of Urban Space
  *3.2. Building of Mitigation-Adaptation Scenarios

** 4.	Results and Actions
    *4.1. Urban Planning, Mitigation and Adaptation to the UHI
    *4.2. Inclusion of the Results into the Planning Process

** 5.	Conclusion

## List of Abbreviations and Acronyms
UHI - Urban Heat Island
UBL - Urban Boundary Layer
UCL - Urban Canopy Layer
LST - Land Surface Temperature
LSE - Land Surface Emissivity
NDVI - Normalized Difference Vegetation Index
TM - Thematic Mapper
ETM+ - Enhanced Thematic Mapper plus
OLI - Operational Land Imager
TIRS - Thermal Infrared Sensor
SNR - Signal to Noise Radiometric
WGS - World Geodetic System
UNESCO - United Nations Educational, Scientific and Cultural Organization
EIA - Environmental Impact Assessments
EPA - Environmental Protection Agency
KMD - Kenya Meteorological Department
CBD - Central Business District
USGS - United States Geological Survey
RGB - Red, Green, Blue Band layers
DMSP/OLS - Defense Meteorological Satellite Program - Operational Linescan System
DN - Digital Number
GIS - Geographic Information System 

## 1.1	INTRODUCTION AND STUDY AREA
  #  1.2	Introduction
In Nairobi City, infill development and urban sprawl are leading to the loss of vegetation and the ratio of land use have increased over the years, these are majorly composed of impervious surfaces such as buildings and parking areas and tarmac roads as well. This therefore has affected the heat balance provided by the natural ecosystem. As warming associated with urban development and climate change intensifies, vulnerable groups will be at risk of heat- related morbidity and mortality. This warming of the city due to the related urbanization and other factors has led to Urban Heat Island effect. The UHI effect is a critical factor for air quality management and public health in urbanized areas all over the world. This effect is relating to an increase in temperatures in urban areas as compared to the surrounding lower density rural areas.
# 1.3	Study Area
The study area is Nairobi, which is the largest city in Kenya and the country’s capital with a focus on the densely urbanized and populated areas. The main focus is the Nairobi which is considered fully urbanized with most surfaces covered with tarmac or various construction materials such as buildings and parking lots. There is maximum land use with minimum vegetation cover compared to the surrounding and during the day and various nights the area is highly populated as much of the activities are carried out in the city Centre. This therefore makes it an ideal area of study for the research topic. It lies in between the latitude 1016’59” South; Longitude 36°49’00’’ East, with an elevation of 1684m above the sea level according to WGS 84 (Latest World Geodetic System) (figure 1.2) 
Figure 1.2 (source: drawn with ArcGIS 10.3): the map showing Nairobi region, study area
Figure 1.3 ( source: Google maps): showing the Nairobi, focused study area. 

# 1.3.1. Study on Urban Heat Island - Project Description

Soon it is expected that the global rate of urbanization will increase by 70% of the present world urban population by 2030. As urban agglomerations emerge and population migration from rural to urban/suburban areas continues, sustainable urban planning faces two major challenges: first the impact of climate change and the necessity for adaptation measures to mitigate the consequences, and second, that of urbanization and the necessity of balancing the various conflicting spatial demands. For to address these issues a comprehensive study on some of the effects related to urbanization is necessary.
Urbanization negatively impacts the environment mainly by the production of pollution, the modification of the physical and chemical properties of the atmosphere and covering of the land surface. Considered to be a cumulative effect of all these impacts is the UHI effect, defined as the rise in temperature in any man-made area, resulting in a well- defined, distinct “warm Island” among “Cool Sea” represented by the lower temperatures of the areas nearby natural landscape. Heat Islands develop when a large fraction of the natural land cover in an area is replaced by built surfaces that trap incoming solar radiation during the day and then re-radiate it at night (Quattro chi et al 200; Oke 1982)) (figure 1.1).
Figure 1.1(source; EPA, 2008): Sketch of an Urban Heat Island Temperature Profile for late afternoon.









**Project Definition: Heat Islands for vulnerable populations**

Urban Heat Islands" (UHIs) refers to urban areas where the temperature is significantly higher than in surrounding areas, due to the concentration of buildings, roads, pavements, and other structures that absorb and retain heat. These areas tend to experience higher temperatures than nearby rural areas, especially during the summer months.

When we talk about "Urban Heat Islands for Vulnerable Populations," we refer to groups of people such as the homeless, migrants, elderly individuals, young children, and people with pre-existing medical conditions. These groups often have less access to resources to protect themselves from extreme heat, such as air conditioning, adequate shelter, or access to clean water.

This situation could lead in health problems as heat strokers or dehydaration. 

# Project description
Project aims to identify urban areas affected by UHIs impacting vulnerable populations. The proposal will propose and develop actionable strategies based on geospatial and weather data to reduce disparities and improve conditions.

# Define
## Research question
How to change conditions and reduce disparities caused by UHIs to improve vulnerable population lives?
## Hypotheses
The mapping and the identification of UHIs can provide guidance to modify those areas. 

## Hypothesis notes
**Find data from the weather systems (forecast and historic) by locations. Areas with high density of vulnerable population to map it. Idenitfy possible solutions and the available resources in the area **
# Find	
## Data sources
* Openstreet map and geospatial data
* Studies and information with solutions to avoud UHIs
* [UHI information](https://www.mdpi.com/2073-4433/12/7/917)
* Data collection weather hystory and forecast
* Identify heat points where vulnerable population are located.
* UHIs information
* Available resources in the area (forests, parks, rivers, sea... )


## Contextual resources


# Get

* Obtain information from areas with populations that are a state of vulnerability, be able to identify the areas and create a map.
   * We classified the data through 3 ranges: (1) a low socioeconomic classification considering TWi values between 0.1 and 0.4; (2) an average socioeconomic classification with TWi values between 0.5 and 0.7; and (3) a high socioeconomic classification consisting of TWi values between 0.8 and 1.
* Get weather information from cities and regions
* Based on studies, find ways to alleviate hot spots.
* Mix everything and, having identified the areas, create proposals based on studies.



## steps
# Verify
## steps
# Clean
## steps
# Analyse
## Analysis plan
## Analysis steps
# Present
## Presentation
