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

apibox = Blueprint('apibox', __name__)


def getVehicleModel():
    # for example
    url = 'https://api.volvocars.com/connected-vehicle/v1/vehicles'
    r = requests.get(url, headers="")
    raw_data = r.json()
    # print(json.dumps(raw_data, indent=4, sort_keys=True))
    vehicleVin = raw_data['data']['vin']

    detailsUrl = 'https://api.volvocars.com/connected-vehicle/v1/vehicles/' + vehicleVin

    res = requests.get(detailsUrl, headers="")

    v_data = res.json()

    vehicleModel = v_data['descriptions']['model']
    
    return vehicleModel
