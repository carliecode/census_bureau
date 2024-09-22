**United States Census Bureau Data Analysis using Apache Spark**



**Project Overview**

This project analyzes the United States Census Bureau's 2017 Basic Monthly CPS data using Apache Spark with Python. The goal is to extract relevant information, answer specific questions, and provide insights into the data.



**Dataset**

- Source: United States Census Bureau's 2017 Basic Monthly CPS
- File: December DOS/Windows zip file (extracted dat file)
- Data Dictionary: Used to map and extract relevant data



**Extracted Data**

The following data was extracted:

1. Full household identifier
2. Time of interview in YYYY/MMM format
3. Final outcome of the survey
4. Type of housing unit
5. Household type
6. Apartment/Household has a telephone
7. Apartment/Household can access a telephone elsewhere
8. Is telephone interview acceptable for the responder
9. Type of interview
10. Family income range
11. Geographical division/location
12. Race



**Analysis Questions**

The following questions were answered:

1. Count of responders per family income range
2. Count of responders per geographical division/location and race (top 10)
3. Number of responders without telephone in their house, but can access a telephone elsewhere and telephone interview is accepted
4. Number of responders who can access a telephone, but telephone interview is not accepted



**Code**

- The code is written in **Python using Apache Spark** and is available in this repository.
- The code uses Jupyter Notebook '**main.ipynb**'.
- Decoding data elements and their corresponding schema information are in **schema.py**.



**Requirements**

- Apache Spark
- Python 3.8
- pandas



**Installation**

1. Install Apache Spark
2. Install required Python libraries using pip install -r requirements.txt
3. Clone this repository
