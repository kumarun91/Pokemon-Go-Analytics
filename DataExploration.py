# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:00:51 2017

@author: muthu
"""

import pandas as py
import matplotlib.pyplot as plt
from matplotlib import dates

pd = py.read_excel('C:/Users/muthu/Desktop/Data/originalDataWithNearestMean.xlsx')

# pandas data Describe
print pd.describe()
from pandas.tools.plotting import scatter_matrix
 
#Scatter matrix
scatter_matrix(pd, figsize=(50,50), diagonal='kde')
plt.show()
plt.savefig("scatter1.png")


# Pearson's correlation coefficient
import numpy as np
d = {}
variables_identified = ['android_ratings_1','android_ratings_2','android_ratings_3','android_ratings_4','android_ratings_5','android_total_ratings','ios_all_ratings']
try:
    for i in range(len(variables_identified)):
        for j in range(i,len(variables_identified)):
            if i != j:    
                rho   =  np.corrcoef(pd[variables_identified[i]].tolist(),pd[variables_identified[j]].tolist()).tolist()
                d[(variables_identified[i],variables_identified[j])] = [rho[0][1]]
except IndexError:
    #print 'Completed Execution'
    pass
try:
    panda = py.DataFrame.from_dict(d, orient='columns', dtype=None)
    panda.to_excel("correlationNearestMean/rho.xlsx")
except ValueError as v:
    print v 
    pass


#TimeSeries graph
xaxisData = []

indexList = pd.index.to_pydatetime().tolist()
xaxisData = dates.date2num(indexList)
variables =['android_average_rating','android_file_size','android_ratings_1','android_ratings_2','android_ratings_3','android_ratings_4','android_ratings_5','android_total_ratings','ios_all_ratings','ios_current_ratings','ios_file_size']
for variable in variables:
    y = pd[variable].tolist()
    fig = plt.figure()
# matplotlib date format object
    hfmt = dates.DateFormatter('%m/%d %H:%M')
    ax1 = fig.add_subplot(1, 1, 1, axisbg='blue')
    ax1.xaxis.set_major_locator(dates.AutoDateLocator())
    ax1.xaxis.set_major_formatter(hfmt)
    ax1.plot(xaxisData, y, 'c', linewidth=3.3)
    plt.xlabel('Date&Time')
    plt.ylabel(variable)
    fig.subplots_adjust(bottom=0.2)
    plt.show()
    plt.savefig('C:/Users/muthu/Desktop/DataScience/Project2/TSGraphs/'+variable+'TimeSeries.jpeg')


