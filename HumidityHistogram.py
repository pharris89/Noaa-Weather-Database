# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:53:29 2022

@author: pharr
"""

#Purpose: Create a histogram of humidity data from the second period
#Name: Paula Harris
#Date: 04/10/2022
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv")
df2 = pd.read_csv("formatdata2.csv")
df2['Humidity'].hist(bins=10, alpha=0.5); plt.suptitle('Histogram of Humidity')
plt.show()
