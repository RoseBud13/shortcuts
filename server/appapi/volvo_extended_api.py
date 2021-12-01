"""
volvoapi.py
- provides the tooling APIs from Volvo.

Created by Xiong, Kaijie on 2021-11-26.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

from flask import Blueprint, jsonify
from flask.json import dumps
import requests
import json
from datetime import datetime


def get_avfuel_consum():
    avfuel_url = "https://api.volvocars.com/extended-vehicle/v1/vehicles/YV4952NA4F120DEMO/resources/averageFuelConsumption"
    res = requests.get(avfuel_url, headers = "")

    a_data = res.json()

    return a_data

def get_av_speed():
    avspeed_url = ""
    res = requests.get(avspeed_url, headers = "")

    a_data = res.json()

    return a_data

def get_battery_remaining():
    batteryremain_url = ""
    res = requests.get(batteryremain_url, headers = "")

    b_data = res.json()

    return b_data

def get_brakefluid():
    brakefluid_url = ""
    res = requests.get(brakefluid_url, headers = "")

    b_data = res.json()

    return b_data

def get_bulb_failure():
    bulbfailure_url = ""
    res = requests.get(bulbfailure_url, headers = "")

    b_data = res.json()

    return b_data

# def distance_to_empty():

def get_enginecoollevel():
    enginecoollevel_url = ""
    res = requests.get(enginecoollevel_url, headers = "")

    e_data = res.json()

    return e_data

def get_enginecooltemp():
    enginecooltemp_url = ""
    res = requests.get(enginecooltemp_url, headers = "")

    e_data = res.json()

    return e_data

def get_engineserhr():
    engineserhr_url = ""
    res = requests.get(engineserhr_url, headers = "")

    e_data = res.json()

    return e_data

def
