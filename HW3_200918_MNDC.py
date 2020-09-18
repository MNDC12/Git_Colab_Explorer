# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 
Last edit on Fri Sep 18
@author: Mary PC
objective: Spyder Explorer
"""

# Import pandas library.
import pandas as pd

# The csv file is in the same folder
df = pd.read_csv('DataSeerGrabPrizeData.csv')  # Read csv file into DataFrame
print('Basic Stat Details:\n{}\n'.format(df.describe()))  # Basic statistical details
print('Data Frame Null:\n{}\n'.format(df.isnull().sum()))  # Number of missing values per column header
df = df.dropna()  # Drop rows of missing values
print('New Data Frame Null:\n{}\n'.format(df.isnull().sum()))  # Number of missing values per column header
print('New Basic Stat Details:\n{}\n'.format(df.describe()))  # Basic statistical details
df.to_csv('NewGrabData3.csv')  # Write object to csv file
