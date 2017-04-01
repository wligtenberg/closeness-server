from flask_diamond import db, ma
from flask_diamond.mixins.crud import CRUDMixin
import datetime

class TemperatureSchema(ma.Schema):
    class Meta:
        additional = ("id", "system_time", "time_stamp_device", "temperature", "client_hash", "participant_number", "study_number")

class Temperature(db.Model, CRUDMixin):
    "A Temperature is a single temperature log for a specific device/participant"
    __schema__ = TemperatureSchema
    __table_args__ = (db.UniqueConstraint('client_hash', 'time_stamp_device', name='_client_time'),)
    id = db.Column(db.Integer(), primary_key=True)
#    mac_address = db.Column(db.String(17))
#    android_id = db.Column(db.String(16))
#    device_id = db.Column(db.String(16))
    system_time = db.Column(db.DateTime, onupdate = datetime.datetime.now)
    time_stamp_device = db.Column(db.DateTime)
    temperature = db.Column(db.Float())
    client_hash = db.Column(db.String(64))
    participant_number = db.Column(db.Integer)
    study_number = db.Column(db.Integer)
