from flask import Flask
import influxdb_client
import influxdb_client
import influxdb_client.client.write_api
from flightsql import FlightSQLClient

app = Flask(__name__)

token = ""
org = ""
url = ""

@app.route("/prediction", methods=['GET'])
def co2_prediction():
    # Connect to InfluxDB
    influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    # Query InfluxDB
    query = """SELECT *
    FROM 'environment'
    WHERE time >= now() - interval '15 days'
    AND ('location' IS NOT NULL)"""

    # Define the query client
    query_client = FlightSQLClient(
    host = "",
    token = token,
    metadata={""})
    
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