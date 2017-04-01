from flask_diamond import db, ma
from flask_diamond.mixins.crud import CRUDMixin
import datetime

class RegisteredDeviceSchema(ma.Schema):
    class Meta:
        additional = ("id", "device_id", "time_stamp", "client_hash")

class RegisteredDevice(db.Model, CRUDMixin):
    "A Registered device is allowed to create Temperatures"
    __schema__ = RegisteredDeviceSchema
    id = db.Column(db.Integer(), primary_key=True)
    device_id = db.Column(db.String(16))
    time_stamp = db.Column(db.DateTime, onupdate = datetime.datetime.now)
    client_hash = db.Column(db.String(64))
