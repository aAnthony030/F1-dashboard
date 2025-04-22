from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import numpy as np
import fastf1
from datetime import datetime
from pages.gare import *
# https://www.f1monkey.com/f1-data-analysis-with-python-the-basics/
# https://openf1.org/
app = Flask(__name__)
fastf1.Cache.enable_cache("cache")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/gare", methods=["GET", "POST"])
def gare():
    location_list = get_liste_dati()
    
    if request.method == "POST":
        selected_location = request.form.get("track")
        
    return render_template("gare.html", tracks=location_list)


@app.route("/get_years", methods=["POST"])
def get_years():
    data = request.get_json()
    track = data.get("track")
    years = get_available_years_for_track(track)
    return jsonify(years)


@app.route("/get_track_data", methods=["GET"])
def get_track_data():
    year = request.args.get("year")
    track = request.args.get("track")

    year = int(year)
    event = fastf1.get_event(year, track)
        
    dati = {
        "EventName": event.EventName,
        "Location": event.Location,
        "Country": event.Country,
        "RoundNumber": event.RoundNumber
    }
        
    return render_template("get_track_data.html", dati=dati)



if __name__ == '__main__':
    app.run(debug=True)