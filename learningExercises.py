# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:48:00 2015

@author: ayla
"""

import pandas as pd # pandas will be referred to as pd below
import numpy as np # because pandas and numpy go hand-in-hand

from pandas import DataFrame, Series # objects of pandas. imported so that 
# we can use them without a pd. prefix.

# Series object: similar to NumPy array but also adds index capabilities
s= Series([1,2,3,4]) # a series with 4 elements, index labels are created automatically 0- based
print (s[[2,3]]) # 2nd and 3rd elements. 0-based

# User-defined (explicit) indexes can also be defined:
s= Series([1,2,3,4], index= ['a', 'b', 'c', 'd'])
print(s[['c','d']])

print(s.index)

# A common usage of a Series in pandas is to represent a time series 
# that associates date/time index labels with a value

# Create a Series whos index values are between two specified dates (inclusive):
dates= pd.date_range('2014-01-01','2014-01-10')

# Let dates represent the index; Create a series with values for each date in the dates 
tempSeries1= Series([15,17,19,21,23,25,27,29,31,33],index= dates)
print(tempSeries1['2014-01-05'])

# DataFrame object is used to have more than one Series of data that is aligned by a column index:
tempSeries2= Series([10,12,14,16,18,20,22,24,26,28],index= dates)
tempDataFrame= DataFrame({'Column1':tempSeries1, 'Column2':tempSeries2})

tempDataFrame.Column1 # returns the first column
tempDataFrame['Column3']= tempDataFrame.Column1 + tempDataFrame.Column2 # Create a new column
tempDataFrame.columns # names of the columns 

tempDataFrame.iloc[0] # get the row array at position 0
tempDataFrame.loc['2014-01-01'] # get the row by index