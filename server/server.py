# encoding=utf-8
import os, glob
import requests
import json
import dateutil.parser
import datetime, time
from shutil import copyfile
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Dashboard Template
from jinja2 import Environment, PackageLoader
jinja_env = Environment(loader=PackageLoader('server', 'views'))


@app.route("/")
def home():
    page = jinja_env.get_template("base.html")
    data = requests.get("https://api.smartcitizen.me/v0/devices/1616")
    resultat= data.json()
    temp=(resultat["data"]["sensors"][2]["value"])
    humid=(resultat["data"]["sensors"][1]["value"])
    batt=(resultat["data"]["sensors"][0]["value"])
    nivso=(resultat["data"]["sensors"][6]["value"])
    Sol=(resultat['data']['sensors'][7]['value'])
    CO=(resultat['data']['sensors'][3]['value'])
    return page.render(temperature =str(temp), humidity=str(humid), batterie=str(batt), nivso=str(nivso), sol=str(Sol), co=str(CO))

@app.route("/clak")
def clak():
    time.sleep(15)
    return "YES"

# Upload snapshot
@app.route("/shot", methods=['POST'])
def shot():
   if request.method == 'POST':
       # check if the post request has the file part
       if 'image' not in request.files:
           return 'ERROR: No file..'

       file = request.files['image']
       if not file or file.filename == '':
           return 'ERROR: Wrong file..'

       # Save Snapshot with Timestamp
       filepath = os.path.join(os.path.dirname(os.path.abspath(__file__))+'/static/upload/', "usershot.jpg")
       file.save(filepath)
       print ("photo enregistree")

       return 'SUCCESS'
   return 'ERROR: You\'re lost Dave..'

if __name__ == "__main__":
   app.run(port=8000)



#changer l
# @app.route("/accueil")
# def accueil():
#     data = requests.get("https://api.smartcitizen.me/v0/devices/1616")
#     resultat= data.json()
#     temperature = resultat["data"]["sensors"][2]["value"]
#     niveau_sonore = resultat["data"]["sensors"][6]["value"]
#
#
#     page = jinja_env.get_template("base.html")
#     return page.render(temp= temperature, nivso= niveau_sonore)
