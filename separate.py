#!/usr/bin/python

import pandas as pd

data = pd.read_csv('games-list.csv')

for col in data.columns:
    if col != 'Year_of_Release' and col != 'Rating':
        data.pop(col)

data = data[data.Rating.notna()]
data = data[data.Year_of_Release.notna()]


data["Year_of_Release"] = data["Year_of_Release"].astype('int')

data_E = data[data['Rating'] == 'E']

data_E10 = data[data['Rating'] == 'E10+']

data_T = data[data['Rating'] == 'T']

data_M = data[data['Rating'] == 'M']


data_E.to_csv (r'./data-E.csv', index = None, header=False, sep = '-') 
data_E10.to_csv (r'./data-E10+.csv', index = None, header=False, sep = '-')
data_T.to_csv (r'./data-T.csv', index = None, header=False, sep = '-') 
data_M.to_csv (r'./data-M.csv', index = None, header=False, sep = '-') 
data.to_csv (r'./data.csv', index = None, header=False, sep = '-') 

