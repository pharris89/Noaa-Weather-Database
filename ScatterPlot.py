# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:56:37 2022

@author: pharr
"""

#Purpose: Create scatter plot of humidity for period 1. Can replace df1 to df2 to display second period data
#Name: Paula Harris
#Date: 04/10/2022
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv")
df2 = pd.read_csv("formatdata2.csv")
plt.scatter(df1.index.values,df1['Humidity']); plt.suptitle('Humidity')
plt.show()
