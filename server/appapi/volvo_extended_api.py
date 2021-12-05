"""
volvoapi.py
- provides the tooling APIs from Volvo.

Created by Xiong, Kaijie on 2021-11-26.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

from flask import Blueprint
import requests
from .config import CredentialConfig

extended_apibox = Blueprint('extended_apibox', __name__)

headersInfo = {}

credentialInfo = CredentialConfig()
headersInfo['authorization'] = getattr(credentialInfo, 'token')
headersInfo['vcc-api-key'] = getattr(credentialInfo, 'vcc_api_key')


class ExtendedApi():
    def get_avfuel_consum():
        avfuel_url = "https://api.volvocars.com/extended-vehicle/v1/vehicles/YV4952NA4F120DEMO/resources/averageFuelConsumption"
        res = requests.get(avfuel_url, headers = headersInfo)

        a_data = res.json()

        return a_data


    def get_av_speed():
        avspeed_url = ""
        res = requests.get(avspeed_url, headers = headersInfo)

        a_data = res.json()

        return a_data


    def get_battery_remaining():
        batteryremain_url = ""
        res = requests.get(batteryremain_url, headers = headersInfo)

        b_data = res.json()

        return b_data


    def get_brakefluid():
        brakefluid_url = ""
        res = requests.get(brakefluid_url, headers = headersInfo)

        b_data = res.json()

        return b_data


    def get_bulb_failure():
        bulbfailure_url = ""
        res = requests.get(bulbfailure_url, headers = headersInfo)

        b_data = res.json()

        return b_data


    def get_enginecoollevel():
        enginecoollevel_url = ""
        res = requests.get(enginecoollevel_url, headers = headersInfo)

        e_data = res.json()

        return e_data


    def get_enginecooltemp():
        enginecooltemp_url = ""
        res = requests.get(enginecooltemp_url, headers = headersInfo)

        e_data = res.json()

        return e_data


    def get_engineserhr():
        engineserhr_url = ""
        res = requests.get(engineserhr_url, headers = headersInfo)

        e_data = res.json()

        return e_data

    def get_trip_meter1():
        tripmeter_url = ""
        res = requests.get(tripmeter_url, headers=headersInfo)

        t_data = res.json()

        return t_data

    def get_trip_meter2():
        tripmeter_url = ""
        res = requests.get(tripmeter_url, headers=headersInfo)

        t_data = res.json()

        return t_data

    def get_odometer():
        odometer_url = ""
        res = requests.get(odometer_url, headers=headersInfo)

        o_data = res.json()

        return o_data

    def get_frontleft_tyre():
        frontleft_tyre_url = ""
        res = requests.get(frontleft_tyre_url, headers=headersInfo)

        f_data = res.json()

        return f_data

