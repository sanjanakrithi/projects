# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:40:01 2019

@author: Miracle
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


payload = {'in_processID' : '10622'}

response = requests.request("POST", url, data=payload)
get = requests.get( url, data=payload)

x = json.loads(response.text)

parser = etree.XMLParser(recover=True)



df = etree.fromstring(x["output_xml"], parser=parser)# root of xml file



app = Flask(__name__)
Bootstrap(app)

@app.route('/home')
def student():
   #return render_template('hello.html')
   #return render_template("unti.html")
   return render_template("pg11.html")
   
@app.route('/',methods = ('POST', 'GET'))
def result():
   #if request.method == 'POST':
      #result = request.form
     return render_template("pg2.html")
     # return render_template("ford2.html")


@app.route('/f1', methods=("POST", "GET"))
def html_table():
    
    return render_template('f1.html')


@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    
    #return 'HI'
    return render_template('x2.html')
      #return render_template('finale5.html')


     
if __name__ == '__main__':
    app.run(debug = True)
