from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import numpy as np
import fastf1
from datetime import datetime
from pages.gare import *
from pages.classifica import *
from pages.home import *
import requests
# https://www.f1monkey.com/f1-data-analysis-with-python-the-basics/
# https://openf1.org/
# TODO: aggiungere libreria slugify
app = Flask(__name__)
fastf1.Cache.enable_cache("cache")


@app.route("/")
def home():
    last_race_result, race_name = get_last_result()
    return render_template("index.html", last_race_result = last_race_result, race_name = race_name)



@app.route("/gare", methods=["GET", "POST"])
def gare():
    years = list(range(2018, 2026))
    sessions = ["SQ", "S", "FP1", "FP2", "FP3", "Q", "R"]
    
    return render_template("gare.html", years=years, session=sessions)



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
    session_type = request.args.get("session", "R")  # di default 'R'
    
    year = int(year)
    
    #In maniera che se si prova ad aggirare il menù di scelta mettendo dati non non validi
    #non dia errori inaspettati da "dati non validi"
    if ((year not in list(range(2018, 2026))) or (track not in get_available_track_for_year(year)) or (session_type not in ["FP1", "FP2", "FP3", "SQ", "S", "Q", "R"])):
        return render_template("get_track_data.html", dati=None, lista_risultati=None, session_type=None)
    
    else:
        event = fastf1.get_event(year, track)
        lista_risultati = session_data(year, event.RoundNumber, session_type, track)

    dati = {
        "EventName": event.EventName,
        "Location": event.Location,
        "Country": event.Country,
        "RoundNumber": event.RoundNumber,
        "Year":year,
        "Session":session_type
    }
        
    return render_template("get_track_data.html", dati=dati, lista_risultati=lista_risultati, session_type=session_type)



@app.route("/classifica", methods=["GET"])
def classifica():
    classifica_piloti = get_classifica_piloti()
    classifica_costruttori = get_classifica_costruttori()
    return render_template("classifica.html", classifica_costruttori=classifica_costruttori, classifica_piloti=classifica_piloti)


if __name__ == '__main__':
    app.run(debug=True)