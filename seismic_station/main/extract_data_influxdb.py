import influxdb_client
import numpy as np

def extract(name):
    token = "YJ5UDkMOWN8bv3eJrs7FgtkpBFJur2BNSYPQt747KDt15516I8hVdEQmPhUp2_bBnOYPAICLuZiHeGFxoZsSbg=="
    org = "nsu"
    bucket = "Seismic"
    url = "http://localhost:8086"
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    query_api = client.query_api()


    query = f"""from(bucket: "Seismic")
     |> range(start: -1000m)
     |> filter(fn: (r) => r._measurement == "trace" and r.location == "{name}")"""

    tables = query_api.query(query, org="nsu")
    trace = np.array([])
    for table in tables:
        for record in table.records:
            trace = np.append(trace, record['_value'])

    return trace
