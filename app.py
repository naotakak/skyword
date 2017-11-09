from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route("/")
def root():
    uResp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=B8khA5bhcMEjHK9mx680bMIPeksDnaT77CFbZ4S1")
    jason = uResp.read()
    d = json.loads(jason)
    return render_template("template.html", title = d["title"], author = d["copyright"], date = d["date"], image = d["url"], caption = d["explanation"])

if __name__ == '__main__':
    app.debug = True
    app.run()
    
