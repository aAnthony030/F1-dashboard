import fastf1

def get_championship_standings(year):
    sessions = ["R", "S"]
    classifica_piloti = []
    
    for session_type in sessions:
        for i in range(1,25):
            session = 1
            
            while session:
                session = fastf1.get_session(year, i, session_type)
                session.load() 
                results = session.results
                
                for _, row in results.iterrows():
                    punti_pilota = {
                    "driver_name": row.BroadcastName,
                    "team": row.TeamName ,
                    "points": int(row.Points)
                    }
                    
                    classifica_piloti.append(punti_pilota)
                    