"""
data_prcss.py
- fetch data from stored files and process them
CI Hub server

Created by Xiong, Kaijie on 2021-09-03.
Copyright © 2021 Volvo Car Corporation. All rights reserved.
"""

import os
import json
from flask import Blueprint

from .apibox import Apibox
from .volvo_connected_api import ConnectedApi
from .volvo_extended_api import ExtendedApi

'''
    Step1: read json
    Step2: parse json to get functions
    Step3: execute fucntions
'''

template_parser = Blueprint('template_parser', __name__)

file_list = []

def run(template_name):
    name = template_name + '.json'
    data_dict = readStoredData(name)
    print(data_dict)
    function_list = get_template_function(data_dict)
    exec_function(function_list)
    return 'executed'


def getAllFileNames():

    temp_file_list = []
    basedir = os.path.abspath(os.getcwd())
    file_path = os.path.join(basedir, 'templates/')

    for f in os.listdir(file_path):
        if not f.startswith('.'):
            temp_file_list.append(f.replace('.json', ''))
    
    file_list = sorted(temp_file_list)
    print(file_list)
    return file_list


def readStoredData(target_file):

    filename = target_file

    basedir = os.path.abspath(os.getcwd()) # this path is for flask app
    # basedir = os.path.dirname(os.getcwd())
    file_path = os.path.join(basedir, 'templates/%s' % filename)

    with open(file_path, 'r') as f:
        data = json.load(f)
    
    return data


def get_template_name(data_dict):
    return data_dict['template_name']


def get_template_function(data_dict):
    function_list = []

    for index in range(len(data_dict['step'])):
        function_dict = data_dict['step'][index]
        for i in function_dict:
            function_list.append(function_dict[i]['function'])
    print(function_list)
    return function_list


def exec_function(funtion_list):
    for i in funtion_list:
        if getattr(Apibox, i, False):
            getattr(Apibox, i, False)()
        elif getattr(ExtendedApi, i, False):
            getattr(ExtendedApi, i, False)()
        elif getattr(ConnectedApi, i, False):
            getattr(ConnectedApi, i, False)()
        else:
            return False


# if __name__ == '__main__':
#     list = getAllFileNames()
#     for i in list:
#         data_dict = readStoredData(i)
#         print(data_dict)
#         print(get_template_name(data_dict))
#         get_template_function(data_dict)
#         function_list = get_template_function(data_dict)
#         exec_function(function_list)



