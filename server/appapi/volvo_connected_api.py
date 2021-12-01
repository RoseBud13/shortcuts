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


# get Vin
def getVehicleVin():
    url = 'https://api.volvocars.com/connected-vehicle/v1/vehicles'
    r = requests.get(url, headers="")
    raw_data = r.json()
    # print(json.dumps(raw_data, indent=4, sort_keys=True))

    vehicleVin = raw_data['data']['vin']
    vehicleUrl = 'https://api.volvocars.com/connected-vehicle/v1/vehicles/' + vehicleVin

    return vehicleUrl

# get vehicle model
def getVehicleModel():
    detailsUrl = getVehicleVin().vehicleUrl
    res = requests.get(detailsUrl, headers = "")
    v_data = res.json()

    vehicleModel = v_data['descriptions']['model']
    
    return vehicleModel


# Endpoint used to get Vehicle's Latest Window Status Values
def getWindowStatus():
    windowUrl = getVehicleVin().vehicleUrl + '/windows'
    res = requests.get(windowUrl, headers = "")
    w_data = res.json()

    Window_info = {}

    window_timestamp = datetime.fromtimestamp(w_data['data']['frontLeft']['timestamp'])
    date = window_timestamp.strftime("%m/%d/%Y, %H:%M:%S")

    Window_info['date'] = date
    Window_info['frontLeft'] = w_data['data']['frontLeft']['value']
    Window_info['frontRight'] = w_data['data']['frontRight']['value']
    Window_info['rearLeft'] = w_data['data']['rearLeft']['value']
    Window_info['rearRight'] = w_data['data']['rearRight']['value']

    return Window_info


# Used to get the vehicle data grouped under warning category such as bulb failure.
def getWarnings():
    warningUrl = getVehicleVin().vehicleUrl + '/warnings'
    res = requests.get(warningUrl, headers = "")
    w_data = res.json()

    Warning_info = {}

    warning_timestamp = datetime.fromtimestamp(w_data['data']['bulbFailure']['timestamp'])
    date = warning_timestamp.strftime("%m/%d/%Y, %H:%M:%S")

    Warning_info['date'] = date
    Warning_info['bulbFailure'] = w_data['data']['bulbFailure']['value']

    return Warning_info


# Endpoint used to get Vehicle's Latest Tyre Status Values
def getTyreStatus():
    tyreUrl = getVehicleVin().vehicleUrl + '/tyres'
    res = requests.get(tyreUrl, headers = "")
    t_data = res.json()

    Tyre_info = {}

    tyre_timestamp = datetime.fromtimestamp(t_data['data']['frontLeft']['timestamp'])
    date = tyre_timestamp.strftime("%m/%d/%Y, %H:%M:%S")

    Tyre_info['date'] = date
    Tyre_info['frontLeft'] = t_data['data']['frontLeft']['value']
    Tyre_info['frontRight'] = t_data['data']['frontRight']['value']
    Tyre_info['rearLeft'] = t_data['data']['rearLeft']['value']
    Tyre_info['rearRight'] = t_data['data']['rearRight']['value']

    return Tyre_info


# get vehicle values grouped under the category of statistics
def getVehicleStat():
    statUrl = getVehicleVin().vehicleUrl + '/statistics'
    res = requests.get(statUrl, headers = "")
    s_data = res.json()

    Vehicle_info = {}
    averageFuelConsumption = {}
    averageSpeed = {}
    tripMeter1 = {}
    tripMeter2 = {}

    date_timestamp = datetime.fromtimestamp(s_data['data']['averageFuelConsumption']['timestamp'])
    date = date_timestamp.strftime("%m/%d/%Y, %H:%M:%S")

    averageFuelConsumption['value'] = s_data['data']['averageFuelConsumption']['value']
    averageFuelConsumption['unit'] = s_data['data']['averageFuelConsumption']['unit']

    averageSpeed['value'] = s_data['data']['averageSpeed']['value']
    averageSpeed['unit'] = s_data['data']['averageSpeed']['unit']

    tripMeter1['value'] = s_data['data']['tripMeter1']['value']
    tripMeter1['unit'] = s_data['data']['tripMeter1']['unit']

    tripMeter2['value'] = s_data['data']['tripMeter2']['value']
    tripMeter2['unit'] = s_data['data']['tripMeter2']['unit']

    Vehicle_info['averageFuelConsumption'] = averageFuelConsumption
    Vehicle_info['averageSpeed'] = averageSpeed
    Vehicle_info['tripMeter1'] = tripMeter1
    Vehicle_info['tripMeter2'] = tripMeter2
    Vehicle_info['date'] = date

    return Vehicle_info


# Endpoint used to read vehicle's latest odometer value in kilometers
def getOdometer():
    OdometerUrl = getVehicleVin().vehicleUrl + '/odometer'
    res = requests.get(OdometerUrl, headers = "")
    o_data = res.json()

    Odometer_info = {}

    date_timestamp = datetime.fromtimestamp(o_data['data']['odometer']['timestamp'])
    date = date_timestamp.strftime("%m/%d/%Y, %H:%M:%S")

    Odometer_info['value'] = o_data['data']['odometer']['value']
    Odometer_info['date'] = date

    return Odometer_info


# get vehicle's latest fuel amount in liters
def getFuel():
    fuelUrl = getVehicleVin().vehicleUrl + '/fuel'
    res = requests.get(fuelUrl, headers = "")
    f_data = res.json()

    Fuel_info = {}

    date_timestamp = datetime.fromtimestamp(f_data['data']['fuelAmount']['timestamp'])
    date = date_timestamp.strftime("%m/%d/%Y, %H:%M:%S")

    Fuel_info['value'] = f_data['data']['fuelAmount']['value']
    Fuel_info['date'] = date

    return Fuel_info


# Environment Values such as external temperature collected by means of Vehicle sensors
def getEnvironment():
    tempUrl = getVehicleVin().vehicleUrl + '/environment'
    res = requests.get(tempUrl, headers = "")
    t_data = res.json()

    Environment_info = {}

    date_timestamp = datetime.fromtimestamp(t_data['data']['externalTemp']['timestamp'])
    date = date_timestamp.strftime("%m/%d/%Y, %H:%M:%S")

    Environment_info['value'] = t_data['data']['externalTemp']['value']
    Environment_info['date'] = date
    return Environment_info


# Vehicle's latest engine diagnostic values such as engine-coolant-level, oil level etc.
def getEngineDiagnostics():
    engineUrl = getVehicleVin().vehicleUrl + '/engine'
    res = requests.get(engineUrl, headers = "")
    e_data = res.json()

    Diagnostics_info = {}

    date_timestamp = datetime.fromtimestamp(e_data['data']['engineRunning']['timestamp'])
    date = date_timestamp.strftime("%m/%d/%Y, %H:%M:%S")

    Diagnostics_info['date'] = date
    Diagnostics_info['engineRunning'] = e_data['data']['engineRunning']['value']
    Diagnostics_info['oilPressure'] = e_data['data']['oilPressure']['value']
    Diagnostics_info['engineCoolantLevel'] = e_data['data']['engineCoolantLevel']['value']
    Diagnostics_info['oilLevel'] = e_data['data']['oilLevel']['value']
    Diagnostics_info['engineCoolantTemp'] = e_data['data']['engineCoolantTemp']['value']

    return Diagnostics_info


# Vehicle's door and lock status values
def getDoorLock():
    statusUrl = getVehicleVin().vehicleUrl + '/doors'
    res = requests.get(statusUrl, headers = "")
    s_data = res.json()

    DoorLock_info = {}

    date_timestamp = datetime.fromtimestamp(s_data['data']['carLocked']['timestamp'])
    date = date_timestamp.strftime("%m/%d/%Y, %H:%M:%S")

    DoorLock_info['date'] = date
    DoorLock_info['lock'] = s_data['data']['carLocked']['value']
    DoorLock_info['frontLeft'] = s_data['data']['frontLeft']['value']
    DoorLock_info['frontRight'] = s_data['data']['frontRight']['value']
    DoorLock_info['hood'] = s_data['data']['hood']['value']
    DoorLock_info['rearLeft'] = s_data['data']['rearLeft']['value']
    DoorLock_info['rearRight'] = s_data['data']['rearRight']['value']
    DoorLock_info['tailGate'] = s_data['data']['tailGate']['value']

    return DoorLock_info

# Used to get the vehicle values grouped under diagnostic category
def getDiagnostic():
    diagnosticUrl = getVehicleVin().vehicleUrl + '/diagnostics'
    res = requests.get(diagnosticUrl, headers = "")
    d_data = res.json()

    Diagnostic_info = {}

    date_timestamp = datetime.fromtimestamp(d_data['data']['serviceStatus']['timestamp'])
    date = date_timestamp.strftime("%m/%d/%Y, %H:%M:%S")

    Diagnostic_info['date'] = date
    Diagnostic_info['serviceStatus'] = d_data['data']['serviceStatus']['value']
    Diagnostic_info['serviceTrigger'] = d_data['data']['serviceTrigger']['value']
    Diagnostic_info['engineHoursToService'] = d_data['data']['engineHoursToService']['value']
    Diagnostic_info['kmToService'] = d_data['data']['kmToService']['value']
    Diagnostic_info['monthToService'] = d_data['data']['monthToService']['value']
    Diagnostic_info['serviceType'] = d_data['data']['serviceType']['value']
    Diagnostic_info['washerFluidLevel'] = d_data['data']['washerFluidLevel']['value']

    return Diagnostic_info


# Used to get the vehicle values grouped under brake category
def getBrakeStatus():
    brakeUrl = getVehicleVin().vehicleUrl + '/brakes'
    res = requests.get(brakeUrl, headers = "")
    b_data = res.json()

    brake_info = {}

    date_timestamp = datetime.fromtimestamp(b_data['data']['brakeFluid']['value'])
    date = date_timestamp.strftime("%m/%d/%Y, %H:%M:%S")

    brake_info['brakeFluid'] = b_data['data']['brakeFluid']['value']
    brake_info['date'] = date

    return brake_info

def postClimatizationStart():
    climatizationUrl = getVehicleVin().vehicleUrl + '/commands/climatization-start'
    API_KEY = ""

    c_data = None

    res = requests.post(url = climatizationUrl, data = c_data)
    action_url = res.text

    return action_url


def postClimatizationStop():
    climatizationUrl = getVehicleVin().vehicleUrl + '/commands/climatization-stop'
    API_KEY = ""

    c_data = None

    res = requests.post(url = climatizationUrl, data = c_data)
    action_url = res.text

    return action_url


def postEngineStart(runtimeMinute):
    engineUrl = getVehicleVin().vehicleUrl + '/commands/engine-start'
    API_KEY = ""

    e_data = {
        "runtimeMinute" : runtimeMinute
    }

    res = requests.post(url = engineUrl, data = e_data)
    action_url = res.text

    return action_url


def postEngineStop():
    engineUrl = getVehicleVin().vehicleUrl + '/commands/engine-stop'

    e_data = None

    res = requests.post(url = engineUrl, data = e_data)
    action_url = res.text

    return action_url


# Used to send a flash command to the vehicle. The vehicles turn signals will flash.
def postFlash():
    flashUrl = getVehicleVin().vehicleUrl + '/commands/flash'

    f_data = None

    res = requests.post(url = flashUrl, data = f_data)
    action_url = res.text

    return action_url


# Used to send a honk and flash command to the vehicle
def postHonkFlash():
    hookflashUrl = getVehicleVin().vehicleUrl + '/commands/honk-flash'

    h_data = None

    res = requests.post(url = hookflashUrl, data = h_data)
    action_url = res.text

    return action_url


# Used to send a honk command to the vehicle
def postHonk():
    honkUrl = getVehicleVin().vehicleUrl + '/commands/honk'

    h_data = None

    res = requests.post(honkUrl, data = h_data)
    action_url = res.text

    return action_url


def postLock():
    lockUrl = getVehicleVin().vehicleUrl + '/commands/lock'

    l_data = None

    res = requests.post(url = lockUrl, data = l_data)
    action_url = res.text

    return action_url


def postUnlock(unlockduration):
    unlockUrl = getVehicleVin().vehicleUrl + '/commands/unlock'

    u_data = {
        "unlockDuration" : unlockduration
    }

    res = requests.post(url = unlockUrl, data = u_data)
    action_url = res.text

    return action_url


def postNavigation(latitude, longitude, name, phone):
    navigationUrl = getVehicleVin().vehicleUrl + '/commands/navi-point-of-interest'

    n_data = {
        "pointOfInterest" : {
            "latitude" : latitude,
            "longitude" : longitude,
            "name" : name,
            "phone" : phone
        }
    }

    res = requests.post(url = navigationUrl, data = n_data)
    action_url = res.text

    return action_url

