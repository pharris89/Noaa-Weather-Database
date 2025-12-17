# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:41:31 2022

@author: pharr
"""

#Purpose: Create box plot for period 2 data
#Name: Paula Harris
#Date: 04/10/2022
import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("formatdata2.csv")
df2.boxplot(); plt.suptitle('Period 2 box plot')
plt.show()
