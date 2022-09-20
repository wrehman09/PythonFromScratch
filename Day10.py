# reading csv , data analyse  using panda 

with open("weather-data.csv") as data_file:
    data=data_file.readlines()
    print(data)

import csv 

with open("weather-data.csv") as data_file:
    data=csv.reader(data_file)
    for row in data:
        print(row[1]) #to read temperature 

import pandas 
data=pandas.read_csv("weather-data.csv")
print(data["temp"])
# there are 2 datatype in panda dataframe (table) and series (column)
data_dict=data.to_dict()
print(data_dict) # to convert data to dictiaonary

#panda has bydefault major functionaluity like maximum, minimum mean etc 