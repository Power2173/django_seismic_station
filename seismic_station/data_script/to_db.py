import sqlite3
import pandas as pd

def to_dbsqlite3():
    data_path = 'data/seismic_stations.csv'
    db_name = 'seismic_station.db'
    table = pd.read_csv(data_path)
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE seismic_stations
                	(station_name TEXT NOT NULL, lat REAL NOT NULL, lon REAL NOT NULL)''')

    for indx, row in table.iterrows():
        cursor.execute('INSERT INTO seismic_stations (station_name, lat, lon) VALUES (?, ?, ?)',
                       (row['name'], row['lat'], row['lon'],))

    connection.commit()
    connection.close()

    return 0

# def get_df():
#     filename = 'seismic_station.db'
#     conn = sqlite3.connect(filename)
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM seismic_stations;")
#     all_results = cur.fetchall()
#     df = pd.DataFrame(all_results, columns = ['name','lat','lon'])
#     return df