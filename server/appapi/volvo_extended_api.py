"""
volvoapi.py
- provides the tooling APIs from Volvo.

Created by Xiong, Kaijie on 2021-11-26.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

from flask import Blueprint, jsonify
import requests
from .config import CredentialConfig

extended_apibox = Blueprint('extended_apibox', __name__)

headersInfo = {}

credentialInfo = CredentialConfig()
headersInfo['authorization'] = getattr(credentialInfo, 'token')
headersInfo['vcc-api-key'] = getattr(credentialInfo, 'vcc_api_key')

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

# def distance_to_empty():

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
