import fastf1
from fastf1.core import Laps
import pandas as pd

# TODO: sistemare i duplicati (monte carlo - monaco) (yas marina - yas island) (le castellet- paul riccard)
# TODO: sistemare problema gestione anni, se nell'url si mettono anni che non sono disponibili in lista,
# tipo 2017, verranno visualizzati i dati, ma non in maniera corretta

# Ricavo gli anni in cui un GP è stato disputato in modo da non mostrare nella scelta
# gli anni in cui il GP non è stato disputato
def get_available_track_for_year(year):
    schedule = fastf1.get_event_schedule(year, include_testing=False)
        
    location_info = schedule["Location"].unique().tolist()
        
    return location_info



def session_data(year, round, session_type, location):
    session = fastf1.get_session(year, round, session_type)
    session.load()
    results = session.results
    lista_risultati = []
    
    for _, row in results.iterrows():
        match session_type:
            case "R" | "S":
                risultato = {
                    "position": int(row.Position),
                    "driver_name": row.BroadcastName,
                    "driver_code": row.Abbreviation,   # Codice abbreviato (VER)
                    "driver_number": str(row.DriverNumber),
                    "team": row.TeamName,
                    "time": str(row.Time)[8:19:],
                    "status": row.Status,
                    "year":year,
                    "location":location,
                    "points": int(row.Points),
                }
                lista_risultati.append(risultato)
            
            case "Q" | "SQ":
                risultato = {
                    "position": int(row.Position),
                    "driver_name": row.BroadcastName,
                    "driver_code": row.Abbreviation,   # Codice abbreviato (VER)
                    "driver_number": str(row.DriverNumber),
                    "team": row.TeamName,
                    "time": str(session.laps.pick_drivers(row.Abbreviation).pick_fastest()["LapTime"])[11:19:],
                    "status": row.Status,
                    "year":year,
                    "location":location,
                }
                lista_risultati.append(risultato)
            
            case "FP1" | "FP2" | "FP3":
                try:
                    time = float(str(session.laps.pick_drivers(row.Abbreviation).pick_fastest()["LapTime"])[13:21:])
                except:
                    time = "//"
    
                risultato = {
                    "driver_name": row.BroadcastName,
                    "driver_code": row.Abbreviation,   # Codice abbreviato (VER)
                    "driver_number": str(row.DriverNumber),
                    "team": row.TeamName,
                    "time": time,
                    "status": row.Status,
                    "year":year,
                    "location":location
                }
                lista_risultati.append(risultato)
                
                
    #Solo se è una session free practice in modo da non fare passaggi inutili in più
    if "FP" in session_type:
        lista_tempi_validi = []
        lista_tempi_vuoti = []
        
        # Prima separazione
        for pilota in lista_risultati:
            if pilota["time"] == "//":
                lista_tempi_vuoti.append(pilota)
            else:
                lista_tempi_validi.append(pilota)
        
        # Applica l'ordinamento di selezione solo sui tempi validi
        for i in range(len(lista_tempi_validi)):
            min_idx = i
            for j in range(i + 1, len(lista_tempi_validi)):
                if float(lista_tempi_validi[j]["time"]) < float(lista_tempi_validi[min_idx]["time"]):
                    min_idx = j
            
            lista_tempi_validi[i], lista_tempi_validi[min_idx] = lista_tempi_validi[min_idx], lista_tempi_validi[i]
        
        #per poter osservare nella classifica i tempi nella maniera corretta
        for i in range(len(lista_tempi_validi)):
            lista_tempi_validi[i]["time"] = "1:" + str(lista_tempi_validi[i]["time"])
            print(lista_tempi_validi[i]["time"])
        lista_risultati = lista_tempi_validi + lista_tempi_vuoti
        
        #Per visualizzare la classifica piloti, in quanto non viene fornita la posizione
        for i in range(len(lista_risultati)):
            lista_risultati[i]["position"] = i + 1
            
    return lista_risultati