'''
    Information display

    General information: Car name / Odometer / Average Fuel Consumption:
    Current car status: remaining battery / Fuel amount / Lock / Tyre pressure
    Diagnostic Values: Service status / Month to service / km to service / Washer fluid level / service Trigger / engineHoursToService / service type
'''

from .volvo_connected_api import ConnectedApi
from .volvo_extended_api import ExtendedApi
from .api import getVModel, getOdo

class Info():

    def general_infomation():
        name = getVModel()
        odo = getOdo()
        avfuelcon = ExtendedApi.get_avfuel_consum()

        general_info_dict = {
            'name' : str(name),
            'Odometer' : str(odo),
            'AverageFuelConsumption' : str(avfuelcon)
        }
        return general_info_dict


    def cur_status():
        # remaining battery
        rebattery = ExtendedApi.get_battery_remaining()

        # tyre
        tyrestatus = ConnectedApi.getTyreStatus()
        tyre_list = []
        for key in tyrestatus:
            if tyrestatus[key] is 'Normal':
                pass
            else:
                tyres = {
                    key : "abnormal"
                }
                tyre_list.append(tyres)
        if len(tyre_list) == 0:
            ftyre_status = 'Normal'
        else:
            ftyre_status = tyre_list

        # fuel amount
        fuelamount = ConnectedApi.getFuel()

        # door, hood, tail gate
        lock_info  = ConnectedApi.getDoorLock()
        lock_list = []
        for key in lock_info:
            if lock_info[key] is 'CLOSED':
                pass
            else:
                lock = {
                    key : "UNLOCKED"
                }
                lock_list.append(lock)

        if len(tyre_list) == 0:
            lock_status = 'CLOSED'
        else:
            lock_status = lock_list

        cur_dict = {
            "remaining battery" : rebattery,
            "tyre" : ftyre_status,
            "lock" : lock_status,
            "fuel" : fuelamount
        }

        return cur_dict


    def home_info():
        general_info = Info.general_infomation()
        cur_info = Info.cur_status()

        result = {k: v for d in [general_info, cur_info] for k, v in d.items()}

        return result


    def dig_info():
        dig_info = ConnectedApi.getDiagnostic()
        return dig_info
        







