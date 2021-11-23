"""
config.py
- settings for the flask application object

Created by Xiong, Kaijie on 2021-11-24.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # used for encryption and session management
    # SECRET_KEY generated from python secrets library
    # secrets.token_hex(16)
    SECRET_KEY = 'da2c44a2527a1b930bbf303b8d4482b7'

