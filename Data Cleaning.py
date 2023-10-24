# -*- coding: utf-8 -*-

#%% Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
np.set_printoptions(threshold=sys.maxsize)
#%% Importing Data
flights_data = pd.read_csv('flights.csv')
print(flights_data.head(10))
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()
print(weather_data_np)
#%% Pandas Data Filtering/Sorting Question Answering
#use flights_data

#Question 1 How many flights were there from JFK to SLC? Int
#q_1
q_1 = len(flights_data[(flights_data['origin']=='JFK') & (flights_data['dest']=='SLC')]) # Filters for flights from JFK to SLC
print('q_1: ',q_1)
#Question 2 How many airlines fly to SLC? Should be int
#q_2
slc = flights_data[flights_data['dest'] == 'SLC']
q_2 = slc['origin'].nunique() #Grab unique airlines, only the unique values get counted
print('q_2: ',q_2)
#Question 3 What is the average arrival delay for flights to RDU? float
#q_3
rdu = flights_data[flights_data['dest'] == 'RDU']
q_3 = rdu['arr_delay'].mean() # .mean() grabs the average
print('q_3: ', q_3)
#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
#q_4
sea = flights_data[flights_data['dest'] == 'SEA']
sea_total = len(sea)
sea_ny = len(sea[(sea['origin']=='JFK') | (sea['origin']=='LGA')]) # | for OR deliniation so we get LGA and JFK airports
q_4 = sea_ny / sea_total
# print(sea_ny)
# print(sea_total)
print('q_4: ', (round(q_4, 2) * 100),'%') #Did this to make it look a little nicer
#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
#q_5
flights_data['Date'] = pd.to_datetime(flights_data[['year', 'month', 'day']]) # Combine these three into one Date column
avg_dep = flights_data[['Date', 'dep_delay']]
avg_dep_grouped = avg_dep.groupby(avg_dep['Date'].dt.date)['dep_delay'].mean()
#print(avg_dep.head())
q_5 = avg_dep_grouped.idxmax() # This will grab the max date
print('q_5: ', q_5)
#Question 6 Which date has the largest average arrival delay? pd slice with date and float
#q_6
avg_arr = flights_data[['Date', 'arr_delay']]
avg_arr_grouped = avg_arr.groupby(avg_arr['Date'].dt.date)['arr_delay'].mean() #grops by the date and ensures proper date forman
#sorted = avg_arr_grouped.sort_values(ascending=False)
# # print(sorted.head())
q_6 = avg_arr_grouped.idxmax()
print('q_6: ', q_6)
#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
#q_7
flights_data['Speed'] = flights_data['distance'] / flights_data['air_time'] #decided to create a Speed column to make this easier
lga_jfk = flights_data[(flights_data['origin']=='JFK') | (flights_data['origin']=='LGA')]
speed = lga_jfk[['tailnum', 'flight', 'Speed']]
fastest = speed['Speed'].max()
q_7 = speed.loc[speed['Speed'] == fastest, 'tailnum'].values[0]
print('q_7: ', q_7)
#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
#q_8
weather_data_pd.fillna(0, inplace=True) #Fills any NA with 0
q_8 = weather_data_pd.isna().any().any() #Checks the entire data frame to see in there are any nans, False if there are none
print('q_8: is_na =', q_8)
#%% Numpy Data Filtering/Sorting Question Answering
#Use weather_data_np
#Question 9 How many observations were made in Feburary? Int
#q_9
feb = weather_data_np[:,3] == 2 #Grab where the month column would be, only if it's 2 for Feb
feb_weath = weather_data_np[feb]
q_9 = len(feb_weath)
print('q_9: ', q_9)
#Question 10 What was the mean for humidity in February? Float
#q_10
humid = feb_weath[:, 8] #now that Feb is filtered, this grabs the humidity column for mean and std calculations
q_10 = np.mean(humid)
print('q_10: ', q_10)
#Question 11 What was the std for humidity in February? Float
#q_11
q_11 = np.std(humid)
print('q_11: ', q_11)
