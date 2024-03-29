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


class CredentialConfig(object):
    token = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkpXVFNJR05FRENFUlQiLCJwaS5hdG0iOiIxNSJ9.eyJzY29wZSI6WyJjb252ZTpicmFrZV9zdGF0dXMiLCJjb252ZTpmdWVsX3N0YXR1cyIsImNvbnZlOmRvb3JzX3N0YXR1cyIsImV4dmU6ZGlhZ25vc3RpY3NfZW5naW5lX3N0YXR1cyIsImFwcG9pbnRtZW50IiwiY29udmU6dHJpcF9zdGF0aXN0aWNzIiwiZXh2ZTpicmFrZV9zdGF0dXMiLCJjb252ZTplbnZpcm9ubWVudCIsImV4dmU6b2RvbWV0ZXJfc3RhdHVzIiwiY29udmU6b2RvbWV0ZXJfc3RhdHVzIiwiY29udmU6aG9ua19mbGFzaCIsImNvbnZlOmNvbW1hbmRfYWNjZXNzaWJpbGl0eSIsImNvbnZlOmVuZ2luZV9zdGF0dXMiLCJjb252ZTpjb21tYW5kcyIsImNvbnZlOnZlaGljbGVfcmVsYXRpb24iLCJjb252ZTp3aW5kb3dzX3N0YXR1cyIsImV4dmU6bG9ja19zdGF0dXMiLCJleHZlOmVuZ2luZV9zdGF0dXMiLCJjb252ZTpuYXZpZ2F0aW9uIiwiY29udmU6dHlyZV9zdGF0dXMiLCJ0c3BfY3VzdG9tZXJfYXBpOmFsbCIsImNvbnZlOmNvbm5lY3Rpdml0eV9zdGF0dXMiLCJhcHBvaW50bWVudDp3cml0ZSIsIm9yZGVyOmF0dHJpYnV0ZXMiLCJjb252ZTpjbGltYXRpemF0aW9uX3N0YXJ0X3N0b3AiLCJleHZlOndhcm5pbmdzIiwiY29udmU6bG9jayIsIm9wZW5pZCIsInByb2ZpbGUiLCJjdXN0b21lcjphdHRyaWJ1dGVzIiwidm9sdm9fb25fY2FsbDphbGwiLCJjb252ZTpkaWFnbm9zdGljc193b3Jrc2hvcCIsImV4dmU6d2luZG93c19zdGF0dXMiLCJjb252ZTp1bmxvY2siLCJjb252ZTpsb2NrX3N0YXR1cyIsImV4dmU6dHlyZV9zdGF0dXMiLCJjdXN0b21lcjphdHRyaWJ1dGVzOndyaXRlIiwiZXh2ZTpkb29yc19zdGF0dXMiLCJleHZlOnZlaGljbGVfc3RhdGlzdGljcyIsImNvbnZlOmRpYWdub3N0aWNzX2VuZ2luZV9zdGF0dXMiLCJleHZlOmZ1ZWxfc3RhdHVzIiwiZXh2ZTpkaWFnbm9zdGljc193b3Jrc2hvcCIsImNvbnZlOndhcm5pbmdzIl0sImNsaWVudF9pZCI6InpmWXM4T0lvIiwiZ3JudGlkIjoibnRGMFdqNzFCMHhWcUtZeG1BWEtBYm11UmQzYXVIMUsiLCJpc3MiOiJodHRwczovL3ZvbHZvaWQuZXUudm9sdm9jYXJzLmNvbSIsImF1ZCI6InpmWXM4T0lvIiwiZmlyc3ROYW1lIjoiQmFsYWppIE5hZ2FyYWoiLCJsYXN0TmFtZSI6Ikt1bWFyIiwic3ViIjoiMTI4YjVlNDgtMmRmMS00Y2M4LTkxODYtYmI2YzU5YTg3NTJjIiwic2NvcGVzIjpbImNvbnZlOmJyYWtlX3N0YXR1cyIsImNvbnZlOmZ1ZWxfc3RhdHVzIiwiY29udmU6ZG9vcnNfc3RhdHVzIiwiZXh2ZTpkaWFnbm9zdGljc19lbmdpbmVfc3RhdHVzIiwiYXBwb2ludG1lbnQiLCJjb252ZTp0cmlwX3N0YXRpc3RpY3MiLCJleHZlOmJyYWtlX3N0YXR1cyIsImNvbnZlOmVudmlyb25tZW50IiwiZXh2ZTpvZG9tZXRlcl9zdGF0dXMiLCJjb252ZTpvZG9tZXRlcl9zdGF0dXMiLCJjb252ZTpob25rX2ZsYXNoIiwiY29udmU6Y29tbWFuZF9hY2Nlc3NpYmlsaXR5IiwiY29udmU6ZW5naW5lX3N0YXR1cyIsImNvbnZlOmNvbW1hbmRzIiwiY29udmU6dmVoaWNsZV9yZWxhdGlvbiIsImNvbnZlOndpbmRvd3Nfc3RhdHVzIiwiZXh2ZTpsb2NrX3N0YXR1cyIsImV4dmU6ZW5naW5lX3N0YXR1cyIsImNvbnZlOm5hdmlnYXRpb24iLCJjb252ZTp0eXJlX3N0YXR1cyIsInRzcF9jdXN0b21lcl9hcGk6YWxsIiwiY29udmU6Y29ubmVjdGl2aXR5X3N0YXR1cyIsImFwcG9pbnRtZW50OndyaXRlIiwib3JkZXI6YXR0cmlidXRlcyIsImNvbnZlOmNsaW1hdGl6YXRpb25fc3RhcnRfc3RvcCIsImV4dmU6d2FybmluZ3MiLCJjb252ZTpsb2NrIiwib3BlbmlkIiwicHJvZmlsZSIsImN1c3RvbWVyOmF0dHJpYnV0ZXMiLCJ2b2x2b19vbl9jYWxsOmFsbCIsImNvbnZlOmRpYWdub3N0aWNzX3dvcmtzaG9wIiwiZXh2ZTp3aW5kb3dzX3N0YXR1cyIsImNvbnZlOnVubG9jayIsImNvbnZlOmxvY2tfc3RhdHVzIiwiZXh2ZTp0eXJlX3N0YXR1cyIsImN1c3RvbWVyOmF0dHJpYnV0ZXM6d3JpdGUiLCJleHZlOmRvb3JzX3N0YXR1cyIsImV4dmU6dmVoaWNsZV9zdGF0aXN0aWNzIiwiY29udmU6ZGlhZ25vc3RpY3NfZW5naW5lX3N0YXR1cyIsImV4dmU6ZnVlbF9zdGF0dXMiLCJleHZlOmRpYWdub3N0aWNzX3dvcmtzaG9wIiwiY29udmU6d2FybmluZ3MiXSwiZW1haWwiOiJiYWxhamkubmFnYXJhai5rdW1hci4yQHZvbHZvY2Fycy5jb20iLCJleHAiOjE2Mzg3NzkzNTZ9.D2fvdF7Maabwxgvlpx6BwJsZYFRZL1owAEhBHkR49clum1hn6p-GY2Nilo4JZaZVwo-u0j3ED6BcKUI2pXZ_QPtJzF1gSYKU0Gl1CJz1J20I6pn9GRaA4QV0EDF6uwOI6LSw6QfVWdxLOzTwGAtnexoSU6vCd-nMNYRQ5S8NJAl4GGWxm0cepWV89ES28qwsS6P_hdSV3nj40GBwJDCNUREBCl-Mp7tu-Jtu5h3RuNXgiwxVrtuzq56WJAlPGv9BaS--XA0aPtO_XtftaIbmJlHrnM_vRuc7KwW9P1K9gKYA_5_iW2LQCk2BxUdDcz8PjrMAOusNlJptJkk5ct3ZAw'
    vcc_api_key = '58a31d0ab3154ca8b57dddb30954444f'

