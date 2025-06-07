import requests

def get_classifica_costruttori():
    url = "https://api.jolpi.ca/ergast/f1/2025/constructorstandings/"

    data = requests.get(url).json()
    classifica_dati_costruttori = data["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"] #Classifica per prendere i dati dei team
    classifica_finale_costruttori = [] #Classifica da mandare a flask

    for i in classifica_dati_costruttori:
        dati = {
            "position":i["position"],
            "team_name":i["Constructor"]["name"],
            "points":i["points"]
        }
        classifica_finale_costruttori.append(dati)

    return classifica_finale_costruttori
   


def get_classifica_piloti():
    url = "https://api.jolpi.ca/ergast/f1/2025/driverstandings/"

    data = requests.get(url).json()
    classifica_dati_piloti = data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"] #Classifica per prendere i dati dei team
    classifica_finale_piloti = [] #Classifica da mandare a flask

    for i in classifica_dati_piloti:
        dati = {
        "position":i["position"],
        "driver_number":i["Driver"]["permanentNumber"],
        "driver_name":i["Driver"]["givenName"] + " " + i["Driver"]["familyName"], #Nome + Cognome
        "driver_team":i["Constructors"][0]["name"],
        "points":i["points"]
        }
        classifica_finale_piloti.append(dati)
    
    return classifica_finale_piloti

print(get_classifica_costruttori())