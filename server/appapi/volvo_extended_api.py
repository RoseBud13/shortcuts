"""
volvoapi.py
- provides the tooling APIs from Volvo.

Created by Xiong, Kaijie on 2021-11-26.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

from flask import Blueprint
import requests
from .config import CredentialConfig
import json

extended_apibox = Blueprint('extended_apibox', __name__)

headersInfo = {}

credentialInfo = CredentialConfig()
headersInfo['authorization'] = getattr(credentialInfo, 'token')
headersInfo['vcc-api-key'] = getattr(credentialInfo, 'vcc_api_key')


class VehicleVin():
    # get Vin and return builded url
    def getVehicleVinUrl():
        url = 'https://api.volvocars.com/extended-vehicle/v1/vehicles'

        print(headersInfo)

        r = requests.get(url, headers = headersInfo)
        raw_data = r.json()
        print(json.dumps(raw_data, indent=4, sort_keys=True))

        vehicleVin = raw_data['data'][0]['vin']
        vehicleUrl = 'https://api.volvocars.com/extended-vehicle/v1/vehicles/' + vehicleVin

        return vehicleUrl

class ExtendedApi():
    def get_avfuel_consum():
        avfuel_url = VehicleVin.getVehicleVinUrl() + "/resources/averageFuelConsumption"
        res = requests.get(avfuel_url, headers = headersInfo)

        a_data = res.json()

        return a_data


    def get_av_speed():
        avspeed_url = VehicleVin.getVehicleVinUrl() + "/resources/averageSpeed"
        res = requests.get(avspeed_url, headers = headersInfo)

        a_data = res.json()

        return a_data


    def get_battery_remaining():
        batteryremain_url = VehicleVin.getVehicleVinUrl() + "/resources/backupBatteryRemaining"
        res = requests.get(batteryremain_url, headers = headersInfo)

        b_data = res.json()

        return b_data


    def get_brakefluid():
        brakefluid_url = VehicleVin.getVehicleVinUrl() + "/resources/brakeFluid"
        res = requests.get(brakefluid_url, headers = headersInfo)

        b_data = res.json()

        return b_data


    def get_bulb_failure():
        bulbfailure_url = VehicleVin.getVehicleVinUrl() + "/resources/bulbFailure"
        res = requests.get(bulbfailure_url, headers = headersInfo)

        b_data = res.json()

        return b_data


    def get_enginecoollevel():
        enginecoollevel_url = VehicleVin.getVehicleVinUrl() + "/resources/engineCoolantLevel"
        res = requests.get(enginecoollevel_url, headers = headersInfo)

        e_data = res.json()

        return e_data


    def get_enginecooltemp():
        enginecooltemp_url = VehicleVin.getVehicleVinUrl() + "/resources/engineCoolantTemp"
        res = requests.get(enginecooltemp_url, headers = headersInfo)

        e_data = res.json()

        return e_data


    def get_engineserhr():
        engineserhr_url = VehicleVin.getVehicleVinUrl() + "/resources/engineHoursToService"
        res = requests.get(engineserhr_url, headers = headersInfo)

        e_data = res.json()

        return e_data

    def get_trip_meter1():
        tripmeter_url = VehicleVin.getVehicleVinUrl() + "/resources/tripMeter1"
        res = requests.get(tripmeter_url, headers=headersInfo)

        t_data = res.json()

        return t_data

    def get_trip_meter2():
        tripmeter_url = VehicleVin.getVehicleVinUrl() + "/resources/tripMeter2"
        res = requests.get(tripmeter_url, headers=headersInfo)

        t_data = res.json()

        return t_data

    def get_odometer():
        odometer_url = VehicleVin.getVehicleVinUrl() + "/resources/odometer"
        res = requests.get(odometer_url, headers=headersInfo)

        o_data = res.json()

        return o_data
