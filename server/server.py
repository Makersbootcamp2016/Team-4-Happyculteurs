# encoding=utf-8
import requests
from flask import Flask
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



if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8000)



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
