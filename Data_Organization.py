# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 23:05:22 2017

@author: arun
"""

from bs4 import BeautifulSoup
import datetime
import pandas as pd
import csv
import json

#outfile1 = open('finaldata.csv','w')
import os


datetimeobj = {}

exhaustiveList=[]
for root, folders, files in os.walk('C:/Users/Arunkumar/Desktop/Project/data/'):
     for eachFolder in folders:
         finalFinalPath = os.path.join(root,eachFolder)
         for path,dirpath,dataFiles in os.walk(finalFinalPath):
             for i in range(len(dataFiles)):
                 exhaustiveList.append(finalFinalPath+'/'+dataFiles[i])
counter = 0.0
for file in exhaustiveList:    
    if file.endswith('_android.html'):
        #counter +=1
        content= open(file).read()
        soup1 =BeautifulSoup(content)
        #android file scraping
        android1 = soup1.find('span',{"class":"reviews-num"})
        android2 = soup1.find('div',{"class":"score"})
        android3 = soup1.find('div',{"class":"rating-bar-container five"})
        android4 = soup1.find('div',{"class":"rating-bar-container four"})
        android5 = soup1.find('div',{"class":"rating-bar-container three"})
        android6 = soup1.find('div',{"class":"rating-bar-container two"})
        android7 = soup1.find('div',{"class":"rating-bar-container one"})
        android8 = soup1.find('div',{"itemprop":"fileSize"})
         
        #outfile1.write(file+"\t")
        
        
        if((android1) and (android2) and (android3) and (android4) and (android5) and (android6) and (android7) and (android8)):
            android_total_ratings = float(android1.get_text().replace(',',''))
            android_average_rating = float(android2.get_text().replace(',',''))
            android_ratings_1 = float(android3.get_text().split()[1].replace(',',''))
            android_ratings_2 = float(android4.get_text().split()[1].replace(',',''))
            android_ratings_3 = float(android5.get_text().split()[1].replace(',',''))
            android_ratings_4 = float(android6.get_text().split()[1].replace(',',''))
            android_ratings_5 = float(android7.get_text().split()[1].replace(',',''))
            android_file_size = float(android8.get_text().strip()[:-1].replace(',',''))
            
            counter += 1
        else:
            android_total_ratings = ''
            android_average_rating = ''
            android_ratings_1 = ''
            android_ratings_2 = ''
            android_ratings_3 = ''
            android_ratings_4 = ''
            android_ratings_5 = ''
            android_file_size = ''
            
        print file
             
    else:
        
        #counter +=1
        content= open(file).read()
        soup2 =BeautifulSoup(content)
            
        ios1 = soup2.find('span',{"itemprop":"reviewCount"})
        ios2 = soup2.find_all('span',{"class":"rating-count"})
        ios3 = soup2.find_all('span',{"class":"label"})
         
        #outfile1.write(file+"\t")
         
        if(ios1 and ios2 and ios3):
            ios_current_ratings = float(ios1.get_text().split()[0].replace(',',''))
            ios_all_ratings = float(ios2[-1].get_text().split()[0].replace(',',''))
            ios_file_size = float(ios3[2].findNext('li').get_text().split()[1].replace(',',''))
            counter += 1
        else:
            ios_current_ratings = ''
            ios_all_ratings = ''
            ios_file_size = ''
               
        print file
        
    
    if(android1 and android2 and android3 and android4 and android5 and android6 and android7 and android8 and ios1 and ios2 and ios3):
        if counter%2 ==0:
        
            temp = file.split('/')
            for eachDate in temp:
                temp1 =temp[6].split('-')
            for eachTime in temp:
                temp2 =temp[7].split('_')[0:2]             
        
            datetimeobj.update({datetime.datetime(int(temp1[0]),int(temp1[1]),int(temp1[2]),int(temp2[0]),int(temp2[1]))
                    :{'android_total_ratings':android_total_ratings,
                       'android_average_rating':android_average_rating,
                       'android_ratings_1':android_ratings_1,
                       'android_ratings_2':android_ratings_2,
                       'android_ratings_3':android_ratings_3,
                       'android_ratings_4':android_ratings_4,
                       'android_ratings_5':android_ratings_5,
                       'android_file_size':android_file_size,
                       'ios_current_ratings':ios_current_ratings,
                       'ios_all_ratings':ios_all_ratings,
                       'ios_file_size':ios_file_size}})

panda = pd.DataFrame(datetimeobj)
tpanda = panda.transpose()


tpanda.to_excel("no_miss_data.xlsx")
tpanda.to_csv("no_miss_data.csv")


with open('no_miss_data.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('no_miss_data.json', 'w') as f:
    json.dump(rows, f)

    
    