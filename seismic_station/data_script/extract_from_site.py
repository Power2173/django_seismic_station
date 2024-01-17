import pandas as pd

def extract_data_from_site():
    table = pd.read_html("http://eqru.gsras.ru/stations/index.php?inc=stalist")
    table_load = table[8]
    table_new = table_load.drop([0, 1])
    col = table_new.columns.tolist()
    columns = ['num', 'int_code', 'reg_code', 'name', 'sei_code', 'lat', 'lon', 'H', 'date_s', 'date_e', 'type']
    table_new.columns = columns
    table_new1 = table_new.drop(columns = 'num', axis = 1)
    table_new1.reset_index(drop=True, inplace = True)

    table_new1.to_csv('data/seismic_stations.csv', index = False, header = True)
    table_new1.to_excel('data/seismic_stations.xlsx', index=False, header=True)
    table_load.to_csv('data/original_seismic_stations.csv')


    return table_new

table = extract_data_from_site()

t = pd.read_csv('data/seismic_stations.csv')
a = t.iloc[0]
b = t.iloc[0].name
c = t.iloc[0]['name']

print('123')

