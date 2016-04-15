from django.shortcuts import render
from django.views.generic import View

from sensor_owner.models import SensorDetails
from influxdb import InfluxDBClient
import json


def connect():
    host = '130.206.113.89'
    port = 8086
    user = 'root'
    password = 'root'
    dbname = 'SensorCloud'
    client = InfluxDBClient(host, port, user, password, dbname)
    return client


def createJson(result):
    available_points = list(result.get_points(measurement='sensor_data'))
    entries = []
    for data in available_points:
        timeVal = data['time']
        value = data['value']
        entries.append({"Time":timeVal, "Value": value})
    json_obj = json.dumps(entries)
    return json_obj

class ShowDashboardView(View):
    def get(self, request):
        influxClient = connect()
        typeOfSensor = 'sea_water_temperature'
        query = 'select time,value from sensor_data'
        result = influxClient.query(query)
        # print result
        jsonObj= createJson(result)
        print jsonObj

        return render(request, 'dashboard.html', {'jsonObj':jsonObj})


