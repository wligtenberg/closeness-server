# -*- coding: utf-8 -*-
# closeness-server (c) Willem Ligtenberg

from flask_restful import Resource
from flask import request
from .models import Temperature as TemperatureModel
from .models import RegisteredDevice as RegisteredDeviceModel
from .models import RegistrationState as RegistrationStateModel
import hashlib as h, random as r, string as s, json, datetime

class RegisteredDevice(Resource):

    def put(self, device_id):
        try:
            reg_state = RegistrationStateModel.find(id=1)
            if reg_state and reg_state.registration_allowed:
                client_hash = h.sha256("".join(r.choice(s.letters+s.digits) for _ in range(64))).hexdigest()
                rd = RegisteredDeviceModel.create(device_id = device_id, client_hash = client_hash, time_stamp = datetime.datetime.now())
                reg_state.registration_allowed = False
                reg_state.update()
                return(client_hash)
            else:
                return("Registration is not possible")
        except:
            return("Error 500")

class Temperature(Resource):

    def put(self):
        all_items = []
        try:
            local_time = datetime.datetime.now()
            json_data = request.form['data']
            temp_data = json.loads(json_data)
            client_hash = temp_data[0]['client_hash']
            rd = RegisteredDeviceModel.find(client_hash = client_hash)
            if rd:
                for item in temp_data:
                    t = TemperatureModel.create(system_time = local_time, time_stamp_device = datetime.datetime.strptime(item['time_stamp_device'], "%Y-%m-%dT%H:%M:%S.%f"), temperature = item['temperature'], client_hash = item['client_hash'], participant_number = item['participant_number'], study_number = item['study_number'])
                    all_items.append(t)
                return("OK")
            else:
                return("Unregistered device")
        except:
            for item in all_items:
                item.delete()
            return("Error 500")
