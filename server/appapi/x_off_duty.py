'''
    Step of off duty:
        1. get external environment(temperature)
            - climatization
        2. Unlock
        3. Engine
        4. navigation
        5. music
'''
from .api import getEnvir
from .volvo_connected_api import postClimatizationStart, postUnlock, postEngineStart, postNavigation
import json

def off_duty(time):

    data = getEnvir()
    json_temp = json.dumps(data)
    data_temp = json.load(json_temp)
    temp = data_temp['value']

    if temp <= 5 or temp >= 25:
        postClimatizationStart()

    result_engine = postEngineStart(runtimeMinute)

    result_nav = postNavigation(latitude, longitude, name, phone)

