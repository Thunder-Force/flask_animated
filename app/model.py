from datetime import datetime
from decimal import Decimal
import json
from flask import request
from urllib import response
import config
import requests

#======================================================================================================================
# USER IP LOCATOR
#======================================================================================================================

class user_ip_loc():
    def get_ip(self):
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            self.ip = request.environ['REMOTE_ADDR']
        else:
            self.ip = request.environ['HTTP_X_FORWARDED_FOR']

    def get_user_ip_info(self):
        self.ip = self.get_ip()
        url = f'https://api.ipgeolocation.io/ipgeo?apiKey={config.IP_GEO_LOC_KEY}&ip=73.169.112.55&fields=all&output=json'
        response = requests.get(url)
        return response.json()      



#======================================================================================================================
# JSON ENCONDER
#======================================================================================================================


class json_encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Decimal):
             return str(obj)
        return json.JSONEncoder.default(self, obj)


