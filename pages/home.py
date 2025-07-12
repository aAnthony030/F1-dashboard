import requests
import fastf1

def get_last_result():
    risultati = []
    round = int(requests.get("https://api.jolpi.ca/ergast/f1/current/last/results").json()["MRData"]["RaceTable"]["Races"][0]["round"])
    year = int(requests.get("https://api.jolpi.ca/ergast/f1/current/last/results").json()["MRData"]["RaceTable"]["Races"][0]["season"])
    race_name = requests.get("https://api.jolpi.ca/ergast/f1/current/last/results").json()["MRData"]["RaceTable"]["Races"][0]["raceName"]

    session = fastf1.get_session(year, round, "R")
    session.load() 
    results = session.results

    for _, row in results.iterrows():
        risultato = {
                "position": int(row.Position),
                "driver_code": row.Abbreviation,   # Codice abbreviato (VER)
                "time": str(row.Time)[8:19:],
                "status": row.Status,
        }
        risultati.append(risultato)

    return risultati, race_name