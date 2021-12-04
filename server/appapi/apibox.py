"""
apibox.py
- provides the tooling APIs from third party.

Created by Xiong, Kaijie on 2021-11-25.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

from flask import Blueprint, jsonify
import requests
import json
from datetime import datetime

apibox = Blueprint('apibox', __name__)


def getDateTime():
    time = datetime.now()
    result = time.strftime("%c")
    return result[:10]


def getWeatherData():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Shanghai&appid=d3ecf245bbd4eeb839a74fc32c366394&units=metric'
    r = requests.get(url)
    raw_data = r.json()
    # print(json.dumps(raw_data, indent=4, sort_keys=True))

    data = {}
    weather_info = {}

    sunrise_timestamp = datetime.fromtimestamp(raw_data['sys']['sunrise'])
    sunset_timestamp = datetime.fromtimestamp(raw_data['sys']['sunset'])
    sunrise = sunrise_timestamp.strftime("%m/%d/%Y, %H:%M:%S")
    sunset = sunset_timestamp.strftime("%m/%d/%Y, %H:%M:%S")
    
    weather_info['description'] = raw_data['weather'][0]['description']
    weather_info['temp'] = raw_data['main']['temp']
    weather_info['feel'] = raw_data['main']['feels_like']
    weather_info['humidity'] = raw_data['main']['humidity']
    weather_info['windspeed'] = raw_data['wind']['speed']
    weather_info['sunrise'] = sunrise[12:]
    weather_info['sunset'] = sunset[12:]
     
    data['location'] = raw_data['name']
    data['weather_status'] = raw_data['weather'][0]['main']
    data['weather_info'] = weather_info
    
    return data