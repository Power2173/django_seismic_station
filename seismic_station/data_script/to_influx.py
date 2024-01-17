import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import numpy as np
import time

token = "YJ5UDkMOWN8bv3eJrs7FgtkpBFJur2BNSYPQt747KDt15516I8hVdEQmPhUp2_bBnOYPAICLuZiHeGFxoZsSbg=="
org = "nsu"
bucket = "Seismic"
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

data = np.random.normal(0, 0.1, 100) + np.sin(np.linspace(0, 20, 100))*10 + np.cos(np.linspace(0, 5, 100))*2
name = 'Аэрологическая'

for i in range(len(data)):
    tracevalue = data[i]
    point = influxdb_client.Point("trace").tag("location", "Аэрологическая").field("tracevalue", float(tracevalue))
    write_api.write(bucket=bucket, org=org, record=point)
    time.sleep(0.1)


# query_api = client.query_api()
#
# query = f"""from(bucket: "Seismic")
#  |> range(start: -100m)
#  |> filter(fn: (r) => r._measurement == "trace" and r.location == "Андозеро")"""
#
# tables = query_api.query(query, org="nsu")
#
# for table in tables:
#   for record in table.records:
#     print(record)

