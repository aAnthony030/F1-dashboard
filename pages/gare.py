import fastf1

# TODO: sistemare i duplicati (monte carlo - monaco) (yas marina - yas island) (le castellet- paul riccard)

# Ricavo gli anni in cui un GP è stato disputato in modo da non mostrare nella scelta
# gli anni in cui il GP non è stato disputato
def get_available_track_for_year(year):
    schedule = fastf1.get_event_schedule(year, include_testing=False)
        
    location_info = schedule["Location"].unique().tolist()
        
    return location_info

'''
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


def session_data(year, round):
    pass

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

'''
import matplotlib.pyplot as plt
import numpy as np
import fastf1
from datetime import datetime

fastf1.Cache.enable_cache('cache')

schedule = fastf1.get_event_schedule(2025)
#print(schedule.columns)
round_info = schedule.loc[:, ["RoundNumber", "Location", "EventDate"]]
round_info_list =  round_info.to_records(index=False).tolist()


#schedule = fastf1.get_event()
#print(schedule)


#https://docs.fastf1.dev/gen_modules/examples_gallery/plot_annotate_corners.html#sphx-glr-gen-modules-examples-gallery-plot-annotate-corners-py
def display_track(year, track_name):
    session = fastf1.get_session(year, track_name, 'Q')
    session.load()

    lap = session.laps.pick_fastest()
    pos = lap.get_pos_data()

    circuit_info = session.get_circuit_info()
    
    #Matrix multiplication, crea le curve
    def rotate(xy, *, angle):
        rot_mat = np.array([[np.cos(angle), np.sin(angle)],
                            [-np.sin(angle), np.cos(angle)]])
        return np.matmul(xy, rot_mat)

    # Get an array of shape [n, 2] where n is the number of points and the second
    # axis is x and y.
    track = pos.loc[:, ('X', 'Y')].to_numpy()

    # Convert the rotation angle from degrees to radian.
    track_angle = circuit_info.rotation / 180 * np.pi

    # Rotate and plot the track map.
    rotated_track = rotate(track, angle=track_angle)
    plt.plot(rotated_track[:, 0], rotated_track[:, 1])
    
    
    offset_vector = [500, 0]  # offset length is chosen arbitrarily to 'look good'

    # Iterate over all corners.
    for _, corner in circuit_info.corners.iterrows():
        # Create a string from corner number and letter
        txt = f"{corner['Number']}{corner['Letter']}"

        # Convert the angle from degrees to radian.
        offset_angle = corner['Angle'] / 180 * np.pi

        # Rotate the offset vector so that it points sideways from the track.
        offset_x, offset_y = rotate(offset_vector, angle=offset_angle)

        # Add the offset to the position of the corner
        text_x = corner['X'] + offset_x
        text_y = corner['Y'] + offset_y

        # Rotate the text position equivalently to the rest of the track map
        text_x, text_y = rotate([text_x, text_y], angle=track_angle)

        # Rotate the center of the corner equivalently to the rest of the track map
        track_x, track_y = rotate([corner['X'], corner['Y']], angle=track_angle)

        # Draw a circle next to the track.
        plt.scatter(text_x, text_y, color='grey', s=140)

        # Draw a line from the track to this circle.
        plt.plot([track_x, text_x], [track_y, text_y], color='grey')

        # Finally, print the corner number inside the circle.
        plt.text(text_x, text_y, txt,
                va='center_baseline', ha='center', size='small', color='white')
        
    plt.title(session.event['Location'])
    plt.xticks([])
    plt.yticks([])
    plt.axis('equal')
    plt.show()

display_track(2024, "Imola")

'''
