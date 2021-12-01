"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses

Created by Xiong, Kaijie on 2021-11-24.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

from flask import Blueprint, jsonify, requests
import random
import requests

from .models import db, Card
<<<<<<< Updated upstream
from .apibox import getWeatherData
from .volvo_connected_api import getVehicleModel
from .volvo_connected_api import getWindowStatus
from .volvo_connected_api import getWarnings
from .volvo_connected_api import getTyreStatus
from .volvo_connected_api import getVehicleStat
from .volvo_connected_api import getOdometer
from .volvo_connected_api import getFuel
from .volvo_connected_api import getEnvironment
from .volvo_connected_api import getEngineDiagnostics
from .volvo_connected_api import getDoorLock
from .volvo_connected_api import getDiagnostic
from .volvo_connected_api import getBrakeStatus
from .volvo_connected_api import postClimatizationStart
from .volvo_connected_api import postClimatizationStop
from .volvo_connected_api import postEngineStart
from .volvo_connected_api import postClimatizationStop
from .volvo_connected_api import postFlash
from .volvo_connected_api import postHonkFlash
from .volvo_connected_api import postHonk
from .volvo_connected_api import postLock
from .volvo_connected_api import postUnlock
from .volvo_connected_api import postNavigation
=======
from .apibox import getWeatherData, getDateTime
from .volvo_connected_api import getVehicleModel, getWindowStatus, getWarnings, getTyreStatus, getVehicleStat, getOdometer, getFuel, getEnvironment, getEngineDiagnostics, getDoorLock, getDiagnostic, getBrakeStatus
from .volvo_connected_api import postClimatizationStart, postClimatizationStop, postEngineStart, postEngineStop, postFlash, postHonkFlash, postHonk, postLock, postUnlock, postNavigation
>>>>>>> Stashed changes


api = Blueprint('api', __name__)


@api.route('/cards-info/', methods=['GET'])
def getCardsInfo():
    cards = Card.query.all()
    return jsonify({'cardsInfo': [card.to_dict() for card in cards]})


@api.route('/car/', methods=['GET'])
def getCar():
    carList = ['XC40', 'XC60']
    carModel = random.choice(carList)
    print(carModel)
    return jsonify({'carModel': carModel})


@api.route('/get-weather/', methods=['GET'])
def getWeather():
    result = getWeatherData()
    return jsonify(result)


# for example
@api.route('/get-v-model/', methods=['GET'])
def getVModel():
    result = getVehicleModel
    return jsonify(result)


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


@api.route('/', methods = ['GET'])
def getStat():
    result = getVehicleStat()
    return jsonify(result)


@api.route('/', methods = ['GET'])
def getOdo():
    result = getOdometer()
    return jsonify(result)


@api.route('/', methods = ['GET'])
def getFuelinfo():
    result = getFuel()
    return jsonify(result)


@api.route('/', methods = ['GET'])
def getFuelinfo():
    result = getFuel()
    return jsonify(result)


@api.route('/', methods = ['GET'])
def getEnvir():
    result = getEnvironment()
    return jsonify(result)


@api.route('/', methods = ['GET'])
def getEngDiag():
    result = getEngineDiagnostics()
    return jsonify(result)


@api.route('/', methods = ['GET'])
def getlock():
    result = getDoorLock()
    return jsonify(result)


@api.route('/', methods = ['GET'])
def getDiag():
    result = getDiagnostic()
    return jsonify(result)


@api.route('/', methods = ['GET'])
def getBrake():
    result = getBrakeStatus()
    return jsonify(result)

<<<<<<< Updated upstream
@api.route('/', methods = ['GET'])
def getBrake():
    result = getBrakeStatus()
    return jsonify(result)
=======

@api.route('/post-climatization-start/', methods = ['POST'])
def postClimStart():
    status = postClimatizationStart()
    return status


@api.route('/post-climatization-stop', methods = ['POST'])
def postClimStop():
    status = postClimatizationStop()
    return status


@api.route('/post-engine-start', methods = ['POST'])
def postEngStart():
    status = postEngineStart()
    return status


@api.route('/post-engine-stop', methods = ['POST'])
def postEngStop():
    status = postEngineStop()
    return status


@api.route('/post-flash', methods = ['POST'])
def postFla():
    status = postFlash()
    return status


@api.route('/post-honkflash', methods = ['POST'])
def postHonFla():
    status = postHonkFlash()
    return status


@api.route('/post-honk', methods = ['POST'])
def postHo():
    status = postHonk()
    return status


@api.route('/post-lock', methods = ['POST'])
def postLo():
    status = postLock()
    return status


@api.route('/post-navigation', methods = ['POST'])
def postNavi():
    status = postNavigation()
    return status

>>>>>>> Stashed changes
