# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:39:26 2019

@author: Miracle
"""
import requests
import json
from xml.etree import ElementTree
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET
from lxml import etree
from xml.etree.ElementTree import XML
from flask import Flask, render_template, request, session, redirect
from flask_bootstrap import Bootstrap


url = "https://na1.ai.dm-us.informaticacloud.com/active-bpel/soap/GetVariable"

querystring = {"wsdl":""}

payload = "{\n\t\"in_processID\" : \"10613\"}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic QVBJX1VzZXI6Q2FsbGl0QDIwMTk=",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "871d2468-ba61-4ff1-9fbe-9304fad82dc2,f36b3efb-75c3-4380-b836-8fa8e73d04d7",
    'Host': "na1.ai.dm-us.informaticacloud.com",
    'accept-encoding': "gzip, deflate",
    'content-length': "28",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
get = requests.get( url, data=payload)
print(response.text)
#x1 = json.loads(response.text)


#parser = etree.XMLParser(recover=True)

tree = ElementTree.fromstring(response.content)

#df = etree.fromstring(tree["sequence"], parser=parser)# root of xml file
tree.getchildren()