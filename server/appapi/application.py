"""
application.py
- creates a Flask app instance and registers the database object

Created by Xiong, Kaijie on 2021-11-24.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

from flask import Flask
from flask_cors import CORS


def create_app(app_name='SHORTCUTXXX'):
    app = Flask(app_name)
    app.config.from_object('appapi.config.BaseConfig')

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    from appapi.api import api
    app.register_blueprint(api, url_prefix="/api")

    from appapi.models import db
    db.init_app(app)

    from appapi.commands import cmd
    app.register_blueprint(cmd)

    from appapi.apibox import apibox
    app.register_blueprint(apibox)

    return app
   