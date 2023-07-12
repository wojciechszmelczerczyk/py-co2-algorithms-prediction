from flask import Flask, jsonify
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from flightsql import FlightSQLClient


app = Flask(__name__)

token = ""
org = ""
url = ""

@app.route("/prediction", methods=['GET'])
def co2_prediction():
    # Connect to InfluxDB
    write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    # Query InfluxDB
    query = """SELECT *
    FROM 'environment'
    WHERE time >= now() - interval '1 hour'
    AND ('bees' IS NOT NULL OR 'ants' IS NOT NULL)"""

    # Define the query client
    query_client = FlightSQLClient(
    host = "",
    token = token,
    metadata={"": ""})
    
    # Execute the query
    info = query_client.execute(query)
    reader = query_client.do_get(info.endpoints[0].ticket)

    # Convert to dataframe
    data = reader.read_all()
    df = data.to_pandas().sort_values(by="time")
    print(df)

    # Return the data as JSON response
    return "hello"


if __name__ == '__main__':
    app.run()