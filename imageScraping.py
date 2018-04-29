# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 23:05:22 2017

@author: arun
"""

from bs4 import BeautifulSoup
import urllib
import os

exhaustiveList=[]
out_folder = 'C:/Users/Arunkumar/Desktop/Project/data/'
for root, folders, files in os.walk(out_folder):
     for eachFolder in folders:
         finalFinalPath = os.path.join(root,eachFolder)
         for path,dirpath,dataFiles in os.walk(finalFinalPath):
             for i in range(len(dataFiles)):
                 exhaustiveList.append(finalFinalPath+'/'+dataFiles[i])

counter1 = 0
counter2 = 0
android2 = set()
ios2 = set()


for file in exhaustiveList:    
    if file.endswith('_android.html'):
        
        content= open(file).read()
        soup1 =BeautifulSoup(content)
        
        #android image scraping
        android1 = soup1.find_all('img',{'class':'screenshot'})
        
        for i in android1:
            android2.add(str(i["src"])) 
            
            
        print file
             
    else:
        
        content= open(file).read()
        soup2 =BeautifulSoup(content)
        
        #ios image scraping
        ios1 = soup2.find_all('img',{'itemprop':'screenshot'})
        
        for i in ios1:
            ios2.add(str(i["src"])) 
        
               
        print file

for j in android2:
    counter1 +=1
    urllib.urlretrieve('http:'+j,'android_screen'+str(counter1)+'.jpeg')    

for j in ios2:
    counter2 += 1
    urllib.urlretrieve(j,'ios_screen'+str(counter2)+'.jpeg') 
    
    

    