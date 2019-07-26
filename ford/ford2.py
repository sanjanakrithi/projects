# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:14:00 2019

@author: Miracle
"""

   
@app.route('/',methods = ('POST', 'GET'))
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("pg2.html")
     # return render_template("ford2.html")


@app.route('/f1', methods=("POST", "GET"))
def html_table():
    return render_template('f1.html')


@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    return 'HI'
    #return render_template('x2.html')
      #return render_template('finale5.html')
