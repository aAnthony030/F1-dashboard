import fastf1

# TODO: sistemare i duplicati (monte carlo - monaco)

#Ricavo gli anni in cui un GP è stato disputato in modo da non mostrare nella scelta
#gli anni in cui il GP non è stato disputato
def get_available_years_for_track(track_name):
    available_years = []

    for year in range(2018, 2026):
        try:
            schedule = fastf1.get_event_schedule(year)
            if track_name in schedule["Location"].values:
                available_years.append(year)
        except Exception as e:
            print(f"Errore con l'anno {year}: {e}")

    return available_years



#Invio i dati sul luogo della pista e che gara stagionale sia
def get_liste_dati():
    
    completed_round_list = []
    completed_location_list = []
    
    for i in range(2018, 2026):
        schedule = fastf1.get_event_schedule(i)
        #print(schedule.columns)
        round_info = schedule.loc[:, ["RoundNumber"]]
        location_info = schedule.loc[:, ["Location"]]
        #date_info = schedule.loc[:, ["EventDate"]]

        round_info_list =  round_info["RoundNumber"].tolist()
        location_info_list =  location_info["Location"].tolist()
        
        completed_round_list.extend(round_info_list)
        completed_location_list.extend(location_info_list)
        #date_info_list =  date_info["EventDate"].tolist()
    
    #Per eliminare tutti i duplicati
    completed_round_list = list(dict.fromkeys(completed_round_list))
    completed_location_list = list(dict.fromkeys(completed_location_list))

    return completed_location_list




