from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import numpy as np
import fastf1
from datetime import datetime
from pages.gare import *

app = Flask(__name__)
fastf1.Cache.enable_cache('cache')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/gare', methods=['GET', 'POST'])
def gare():
    location_list = get_liste_dati()
    selected_location = None
    
    if request.method == 'POST':
        selected_location = request.form.get('track')
        
    return render_template('gare.html', tracks=location_list)


@app.route('/get_years', methods=['POST'])
def get_years():
    data = request.get_json()
    track = data.get("track")
    years = get_available_years_for_track(track)
    return jsonify(years)


if __name__ == '__main__':
    app.run(debug=True)
