from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import numpy as np

# token = "yn2LAGEv2E6UeqskUBT1ju48fZqBMG-0_THJEWxTWyUUr8byHKZJCLPHRyI-3mdLteUoCRuIs3EqjG92gZx5PA=="
token = "YJ5UDkMOWN8bv3eJrs7FgtkpBFJur2BNSYPQt747KDt15516I8hVdEQmPhUp2_bBnOYPAICLuZiHeGFxoZsSbg=="
org = "nsu"
bucket = "Seismic"

client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)


class InfluxClient:
    def __init__(self, token, org, bucket):
        self._org = org
        self._bucket = bucket
        self._client = InfluxDBClient(url="http://localhost:8086", token=token)

    def write_data(self, data, write_option=SYNCHRONOUS):
        write_api = self._client.write_api(write_option)
        write_api.write(self._bucket, self._org, data, write_precision='s')

    def query_data(self, query):
        query_api = self._client.query_api()
        result = query_api.query(org=self._org, query=query)
        trace = np.array([])
        for table in result:
            for record in table.records:
                trace.append(record["_value"])
        return trace

    def delete_data(self, measurement):
        delete_api = self._client.delete_api()
        start = "1970-01-01T00:00:00Z"
        stop = "2021-10-30T00:00:00Z"
        delete_api.delete(start, stop, f'_measurement="{measurement}"', bucket=self._bucket, org=self._org)


IC = InfluxClient(token, org, bucket)

def get_data_influx(name):
    query = f"""from(bucket: "Seismic")
     |> range(start: -1000m)
     |> filter(fn: (r) => r._measurement == "trace" and r.location == {name})"""
    data = IC.query_data(query)
    return np.array(data, dtype='float32')