from flask_diamond import db
from flask_diamond.mixins.crud import CRUDMixin

class Registered_Device(db.Model, CRUDMixin):
    "A Registered device is allowed to create Temperatures"
    id = db.Column(db.Integer(), primary_key=True)
    device_id = db.Column(db.String(16))
    time_stamp = db.Column(db.DateTime)
    client_hash = db.Column(db.String(64))
