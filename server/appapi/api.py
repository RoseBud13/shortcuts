"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses

Created by Xiong, Kaijie on 2021-11-24.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

from flask import Blueprint, jsonify
import random

from .models import db, Card
from .apibox import getWeatherData, getDateTime
from .volvo_connected_api import getVehicleModel, getWindowStatus, getWarnings, getTyreStatus, getVehicleStat, getOdometer, getFuel, getEnvironment, getEngineDiagnostics, getDoorLock, getDiagnostic, getBrakeStatus
from .volvo_connected_api import postClimatizationStart, postClimatizationStop, postEngineStart, postFlash, postHonkFlash, postHonk, postLock, postUnlock, postNavigation


api = Blueprint('api', __name__)


@api.route('/cards-info/', methods=['GET'])
def getCardsInfo():
    cards = Card.query.all()
    return jsonify({'cardsInfo': [card.to_dict() for card in cards]})


# for example
@api.route('/car/', methods=['GET'])
def getCar():
    carList = ['XC40', 'XC60']
    carModel = random.choice(carList)
    print(carModel)
    return jsonify({'carModel': carModel})


@api.route('/get-datetime/', methods=['GET'])
def getDateInfo():
    result = getDateTime()
    return jsonify({'dateInfo': result})


@api.route('/get-weather/', methods=['GET'])
def getWeather():
    result = getWeatherData()
    return jsonify(result)


# for example
@api.route('/get-v-model/', methods=['GET'])
def getVModel():
    result = getVehicleModel()
    return result


@api.route('/vcc-api-windowsStatus/', methods = ['GET'])
def getWinStatus():
    result = getWindowStatus()
    return jsonify(result)


@api.route('/vcc-api-key/', methods = ['GET'])
def getWarnStatus():
    result = getWarnings()
    return jsonify(result)


@api.route('/vcc-api-key/', methods = ['GET'])
def getTyre():
    result = getTyreStatus()
    return jsonify(result)


@api.route('/get-v-stat/', methods = ['GET'])
def getStat():
    result = getVehicleStat()
    return jsonify(result)


@api.route('/get-odo/', methods = ['GET'])
def getOdo():
    result = getOdometer()
    return jsonify(result)


@api.route('/get-fuel-info/', methods = ['GET'])
def getFuelinfo():
    result = getFuel()
    return jsonify(result)


@api.route('/get-env-temp/', methods = ['GET'])
def getEnvir():
    result = getEnvironment()
    return jsonify(result)


@api.route('/get-eng-diag/', methods = ['GET'])
def getEngDiag():
    result = getEngineDiagnostics()
    return jsonify(result)


@api.route('/get-door-lock-status/', methods = ['GET'])
def getLockStatus():
    result = getDoorLock()
    return jsonify(result)


@api.route('/get-v-diag/', methods = ['GET'])
def getDiag():
    result = getDiagnostic()
    return jsonify(result)


@api.route('/get-brake-status/', methods = ['GET'])
def getBrake():
    result = getBrakeStatus()
    return jsonify(result)
