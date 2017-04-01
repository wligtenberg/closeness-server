from flask_diamond import db
from flask_diamond.mixins.crud import CRUDMixin

class Temperature(db.Model, CRUDMixin):
    "A Temperature is a single temperature log for a specific device/participant"
    id = db.Column(db.Integer(), primary_key=True)
    mac_address = db.Column(db.String(17))
    android_id = db.Column(db.String(16))
    device_id = db.Column(db.String(16))
    system_time = db.Column(db.DateTime)
    time_stamp_device = db.Column(db.DateTime)
    temperature = db.Column(db.Float())
    client_hash = db.Column(db.String(64))
    participant_number = db.Column(db.Integer)
    study_number = db.Column(db.Integer)
