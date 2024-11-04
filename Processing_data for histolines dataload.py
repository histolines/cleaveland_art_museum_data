# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:00:50 2024

@author: tapac
"""

import re
import time

import pandas as pd


data = pd.read_excel('data.xlsx', sheet_name = 'data')

eventDetail=data['image_web']
ref=data['url']


#### Clean and append names of artists to the list
whoCharName=[]
for name in data['creators']:
    
    ##whoCharName[1]
    ##name=whoCharName[1]
    ##name.find("(")
    name=name.replace(u'\xa0', u' ').replace("'","").replace('"',"").replace('/',",").strip().replace("'s","")
    name=name.replace('É',"E").replace('é',"e").replace('á',"a").replace("'","").replace("Hilaire Germain ","").replace("ü","u").replace("è","e").replace("ç","c").replace("ó","o").replace("’","")      .replace("https:","")        
                
    name_clean=name[:name.find("(")-1]
    whoCharName.append(name_clean)
    
    
  #### Clean and append  description  
whatRef=[]
for name in data['technique']:
    try:
        name=name.replace(u'\xa0', u' ').replace("'","").replace('"',"").replace('/',",").strip().replace("'s","")
        name=name.replace('É',"E").replace('é',"e").replace('á',"a").replace("'","").replace("Hilaire Germain ","").replace("ü","u").replace("è","e").replace("ç","c").replace("ó","o").replace("’","")      .replace("https:","")        
        whatRef.append(name) 
    except:
        whatRef.append("") 

  #### Clean and append artwork name   
whoRel=[]
for name in data['title']:
    try:
        name=name.replace(u'\xa0', u' ').replace("'","").replace('"',"").replace('/',",").strip().replace("'s","s")
        name=name.replace('É',"E").replace('é',"e").replace('á',"a").replace("'","").replace("Hilaire Germain ","").replace("ü","u").replace("è","e").replace("ç","c").replace("ó","o").replace("’","")      .replace("https:","")   .replace("Ō","O")  .replace("ō","o")     
        whoRel.append("artwork "+name) 
    except:
        whoRel.append("") 
#### Clean and append year and record id
whenYear=[]
lates_id= 1254741
eventId=[]
for i in range(len(data['creation_date_earliest'])):
    try:
        start =data['creation_date_earliest'][i]
        end=data['creation_date_latest'][i]
        mid=int((start+end)/2)
        whenYear.append(mid)
    except:
        whenYear.append(9999)
   
    eventId.append(lates_id+1+i)

#### Clean and append all the other fields with constants
whatEventtype=[]
enterDate=[]
orgCont=[]
whenMonth=[]
whenDay=[]
whereLat=[]
whereLon=[]
whereLoc=[]
eventSig=[]
eventAccYes=[]
eventAccNo=[]

for name in data['technique']:
    whatEventtype.append('took a picture')
    enterDate.append('2024-07-12')
    orgCont.append('ClevelandMuseumArt')
    whenMonth.append(0)
    whenDay.append(0)
    whereLat.append(0)
    whereLon.append(0)
    whereLoc.append("")
    eventSig.append(3)
    eventAccYes.append(0)
    eventAccNo.append(0)
    


    
    
    
    
  #combining to create  load data dataframe
    
loaddata = pd.DataFrame()
loaddata['eventId']= eventId   
loaddata['whoCharName']= whoCharName
loaddata['whatEventType']= whatEventtype  
loaddata['whenYear']= whenYear
loaddata['whenMonth']= whenMonth
loaddata['whenDay']= whenDay
loaddata['whereLat']= whereLat 

loaddata['whereLon']= whereLon 
loaddata['whereLoc']= whereLoc
loaddata['whoRel']= whoRel
loaddata['whatRef']= whatRef  
loaddata['enterDate']= 	enterDate
loaddata['eventSig']= eventSig
loaddata['eventAccYes']= eventAccYes
loaddata['eventAccNo']= eventAccNo
loaddata['orgCont']= orgCont
loaddata['eventDetail']= data['image_web']
loaddata['ref']= data['url']


### filtering the load data dataframe

loaddata=loaddata[loaddata.whenYear != "0s"]
loaddata=loaddata[loaddata.whenYear != 9999]
loaddata=loaddata[loaddata.whoCharName != ""]

loaddata=loaddata[loaddata.eventDetail != "nan"]
loaddata=loaddata[loaddata.eventDetail.str.len() > 5]
loaddata=loaddata[loaddata.whenYear != "0"].reset_index(drop=True)



loaddata_ref= pd.DataFrame()
loaddata_ref['eventId']=loaddata['eventId']
loaddata_ref['ref']=loaddata['ref']
loaddata_ref.to_csv('loaddata_ref.csv', index=False, header=False)


loaddata=loaddata.drop(columns=['ref'])
loaddata.to_csv('loaddata.csv', index=False, header=False)






