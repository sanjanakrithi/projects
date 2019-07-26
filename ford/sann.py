# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:05:40 2019

@author: kumar
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:04:41 2019

@author: kumar
"""

import requests
import json
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET
from lxml import etree
from xml.etree.ElementTree import XML
from flask import Flask, render_template, request, session, redirect
from flask_bootstrap import Bootstrap

url = "https://na1.ai.dm-us.informaticacloud.com/active-bpel/public/rt/5Yg7jlWxU46jbQLX3VaL07/GetVariable"


payload = {'in_processID' : '10108'}

response = requests.request("POST", url, data=payload)
get = requests.get( url, data=payload)#gets the url with the payload
x = json.loads(response.text)
from lxml import etree
parser = etree.XMLParser(recover=True)

df = etree.fromstring(x['output_xml'], parser=parser)# root of xml file
#print(df)
#response_xml_as_string = "xml response string from API"
#responseXml = ET.fromstring(df)
'''
'''
#testId = df.find('name').find('text')
#print (testId.text)
#root = ET.fromstring(get.content)

''', headers=headers'''
'''
#new method for trail
#print(response.text)
x = json.loads(response.text)
from lxml import etree
parser = etree.XMLParser(recover=True)

#root = parser.getroot()


# root = parser.getroot()
df = etree.fromstring(x['output_xml'], parser=parser)# root of xml file
from lxml import etree
## using a function to parse and print the output
def parseXML(xmlFile):
    """
    Parse the xml
    """
    with open(xmlFile) as fobj:
        xml = fobj.read()

    root = etree.fromstring(xml)

    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            print(elem.tag + " => " + text)

if __name__ == "__main__":
    parseXML("df")
  
    

df = etree.fromstring(x['output_xml'], parser=parser)# root of xml file
for event, element in etree.iterparse(df, tag="name"):
    for child in element:
        print (child.tag, child.text)
    element.clear()


## old and working method
'''

df = etree.fromstring(x['output_xml'], parser=parser)# root of xml file

df_cols = ["value"]
df_rows =["Text"]
#out_df = pd.Series()
out_df1 = pd.DataFrame(columns = df_cols)
for element in  df.iter(tag= 'text'):
   
    s_mail = element.text
    
    
    out_df1 = out_df1.append(pd.Series([ s_mail], index = ['value']), ignore_index=True)
    
    

print(out_df1 )
out_df = pd.DataFrame(columns = df_rows)
for element in  df.iter(tag= 'name'):
    s_mail = element.text

    out_df = out_df.append(pd.Series([ s_mail], index = ['labels']), ignore_index=True)
print(out_df )
#result = pd.concat([out_df1, out_df], axis=1, sort=False)
#print(result)
result = pd.concat([out_df1, out_df], axis=1, join_axes=[out_df1.index])
print(result)

#modDfObj = result.drop('Text' , axis='columns')
#print(modDfObj)
#df1 = modDfObj['labels']
#print(df1)




#df10 = pd.Series([df1])
#print(df10)
from pandas import DataFrame



df = DataFrame(out_df, columns= ['labels'])

listd = df.values.tolist()
print (listd)
df1 = DataFrame(out_df1, columns= ['value'])

list1 = df1.values.tolist()
print (list1)
list2 = DataFrame(list1)
print(list2)

#listd.append(list1)
#print (listd)
#l = listd+list1
#print(l)
df20 = pd.DataFrame([listd])
print(df20)
df30 = pd.DataFrame([list1])
print(df30)
#x = df30.drop(['current_user'], axis=1)
#print(x)
#y = df20.drop(['current_user','process_title'], axis=1)
#print(y)
#dfObj = pd.DataFrame(df20, columns = ['input','in_status','current user','process title'])
#print(dfObj)
df4 = df20.append(df30, ignore_index=True)
print(df4)

#x.to_html('finale4.html')
df4.to_html('f1.html')


