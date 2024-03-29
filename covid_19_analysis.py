# -*- coding: utf-8 -*-
"""Covid-19_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gWq46Vok3SKnoSG2e0YFlw7fRAl1ZKUf

## **Project Summary**

The "Covid-19 Analysis" provides a real-time, data-driven overview of the global COVID-19 pandemic. It offers visualizations of key metrics, such as confirmed cases, deaths, and recoveries, allowing users to explore trends, compare countries, and stay informed about the latest developments. The dashboard serves as a valuable tool for researchers, policymakers, and the public to monitor and analyze the impact of the virus worldwide.

##Import Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Mounting the google drive to access the files
from google.colab import drive
drive.mount('/content/drive')

"""### Loading the Dataset"""

covid = pd.read_csv('/content/drive/MyDrive/covid_19_data.csv')

"""### Dataset First View"""

covid.head()

covid.tail()

"""### Dataset Rows & Columns count"""

# Get the count of rows and columns
num_rows, num_columns = covid.shape

# Display the count
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

"""There are 45179 Rows and 8 Columns in this Dataset.

## Dataset Info
"""

covid.info()

# Checking the shape of the dataframe
covid.shape

# Missing Values/Null Values Count
covid.isnull().sum().sum()

"""There are total 19029 null values in the dataset."""

covid.drop('SNo',axis=1,inplace=True)

covid['ObservationDate'] = pd.to_datetime(covid['ObservationDate'])

covid.info()

covid.head()

covid = covid.set_index('ObservationDate')

datewise_covid = covid.groupby(['ObservationDate']).agg({'Confirmed': 'sum','Deaths':'sum','Recovered':'sum'})

datewise_covid.head()

sns.set_style('darkgrid')
plt.figure(figsize=(15,12))
sns.barplot(x = datewise_covid.index.date,y = datewise_covid['Confirmed'],palette='YlOrRd')
plt.xticks(rotation=90)
plt.title('Datewise Confirmed Cases')

#A mortality rate is a measure of the frequency of occurrence of death in a defined population during a specified interval.
datewise_covid['Mortality Rate'] = (datewise_covid['Deaths']/datewise_covid['Confirmed'])*100

datewise_covid.head()

plt.figure(figsize=(12,6))
plt.plot(datewise_covid['Mortality Rate'],label="Mortality Rate")
#plt.xticks(rotation=90)
plt.show()

India_data = covid[covid['Country/Region']=='India']

datewise_india = India_data.groupby(['ObservationDate']).agg({'Confirmed': 'sum','Deaths':'sum','Recovered':'sum'})

datewise_india.head()

datewise_india['Mortality Rate'] = (datewise_india['Deaths']/datewise_india['Confirmed'])*100

plt.figure(figsize=(12,6))
plt.plot(datewise_india['Mortality Rate'],label="Mortality Rate")
plt.xticks(fontsize=18)
plt.show()

datewise_india['Recovery Rate'] = (datewise_india['Recovered']/datewise_india['Confirmed'])*100

plt.figure(figsize=(12,6))
plt.plot(datewise_india['Mortality Rate'],label="Mortality Rate")
plt.xticks(fontsize=18)
plt.show()

datewise_india['Recovery Rate'] = (datewise_india['Recovered']/datewise_india['Confirmed'])*100

plt.figure(figsize=(12,6))
plt.plot(datewise_india['Recovery Rate'],label="Recovery Rate")
plt.xticks(fontsize=18)
plt.show()

plt.figure(figsize=(12,6))
datewise_india['Confirmed'].diff().plot()

plt.figure(figsize=(12,6))
datewise_india['Recovered'].diff().plot()

plt.figure(figsize=(12,6))
datewise_india['Mortality Rate'].diff().plot()

plt.figure(figsize=(12,6))
datewise_india['Recovery Rate'].diff().plot()