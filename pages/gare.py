import fastf1

# TODO: sistemare i duplicati (monte carlo - monaco)

# Ricavo gli anni in cui un GP è stato disputato in modo da non mostrare nella scelta
# gli anni in cui il GP non è stato disputato
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



# Invio i dati sul luogo della pista e che gara stagionale sia
def get_liste_dati():
    completed_location_list = []
    
    for i in range(2018, 2026):
        schedule = fastf1.get_event_schedule(i, include_testing=False)
        
        location_info = schedule.loc[:, ["Location"]]
   
        location_info_list =  location_info["Location"].tolist()
        
        completed_location_list.extend(location_info_list)
        
    # Per eliminare tutti i duplicati
    completed_location_list = list(dict.fromkeys(completed_location_list))
    #dict_location_round_for_year = get_location_year_round_map()
    
    return completed_location_list


'''
Non so perchè cazzo ho fatto questo, ma l'ho fatto, dopo lo sforzo mio e di chat per farlo lo lasciero
qui sperando che in un futuro mi tornerà utile

# Metto in un dizionario le piste con i rispetivvi anni in cui si è corso, se non si è corso quell'anno
# verrà messo '0', senno verrà inserita la posizione corrispondente al calendario di quell'anno
def get_location_year_round_map():
    # Lista anni da considerare
    years = list(range(2018, 2026))
    
    # Dizionario che conterrà: {location: [round_per_anno]}
    location_year_map = {}

    for year in years:
        schedule = fastf1.get_event_schedule(year, include_testing=False)
        
        for _, row in schedule.iterrows():
            location = row["Location"]
            round_number = row["RoundNumber"]
            
            # Se la location non esiste nel dizionario, la inizializziamo con zeri
            if location not in location_year_map:
                location_year_map[location] = [0] * 8 # cioè len(years)
            
            # Inseriamo il round_number nella posizione corrispondente all'anno
            index = years.index(year)
            location_year_map[location][index] = round_number

    return location_year_map
'''