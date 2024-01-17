import sqlite3
import pandas as pd

def get_data():
    filename = 'static/seismic_station.db'
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute("SELECT * FROM seismic_stations;")
    all_results = cur.fetchall()
    data = pd.DataFrame(all_results, columns = ['name','lat','lon'])

    return data