# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:41:31 2022

@author: pharr
"""

#Purpose: Create box plot for period 3 data
#Name: Paula Harris
#Date: 04/10/2022
import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv("formatdata3.csv")
df3.boxplot(); plt.suptitle('Period 3 box plot')
plt.show()
