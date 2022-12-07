#!/usr/bin/python

import pandas as pd

data = pd.read_csv('games-list.csv')

data = data.dropna()

data["Year_of_Release"] = data["Year_of_Release"].astype('int')

data = data.replace(',','', regex = True)

print(data)

data.to_csv (r'./data.csv', index = None, header = False) 
