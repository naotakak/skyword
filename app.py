'''
Naotaka Kinoshita
SoftDev1 Pd7
K#13: A RESTful Journey Skyward
2017-11-10
'''

from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/wunder")
def wunder():
    uResp = urllib2.urlopen("http://api.wunderground.com/api/750c29e1e9c579bc/conditions/q/NY/New_York.json")
    jason = uResp.read()
    d = json.loads(jason)
    radar = "http://api.wunderground.com/api/750c29e1e9c579bc/animatedradar/q/NY/New_York.gif?newmaps=1&timelabel=1&timelabel.y=10&num=5&delay=50"
    return render_template("weather.html", full = d["current_observation"]["display_location"]["full"], zip = d["current_observation"]["display_location"]["zip"], weather = d["current_observation"]["weather"], temp = d["current_observation"]["temperature_string"], humidity = d["current_observation"]["relative_humidity"], radar = radar)

@app.route("/nasa")
def nasa():
    uResp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=B8khA5bhcMEjHK9mx680bMIPeksDnaT77CFbZ4S1")
    jason = uResp.read()
    d = json.loads(jason)
    return render_template("template.html", title = d["title"], author = d["copyright"], date = d["date"], image = d["url"], caption = d["explanation"])

if __name__ == '__main__':
    app.debug = True
    app.run()
    
