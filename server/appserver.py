"""
appserver.py
- creates an application instance for running the server

Created by Xiong, Kaijie on 2021-11-24.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

if __name__ == '__main__':
    from appapi.application import create_app
    app = create_app()
    app.run()
