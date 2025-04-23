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
    years = list(range(2018, 2025))
    return render_template("gare.html", years=years)


@app.route("/get_tracks", methods=["POST"])
def get_years():
    data = request.get_json()
    year = int(data.get("year"))
    
    track_list = get_available_track_for_year(year)
    return jsonify(track_list)


@app.route("/get_track_data", methods=["GET"])
def get_track_data():
    year = request.args.get("year")
    track = request.args.get("track")

    year = int(year)
    event = fastf1.get_event(year, track)
    
    session_data(year, event.RoundNumber)
    
    dati = {
        "EventName": event.EventName,
        "Location": event.Location,
        "Country": event.Country,
        "RoundNumber": event.RoundNumber
    }
        
    return render_template("get_track_data.html", dati=dati)



if __name__ == '__main__':
    app.run(debug=True)