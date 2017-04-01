from flask_diamond import db, ma
from flask_diamond.mixins.crud import CRUDMixin

class RegistrationStateSchema(ma.Schema):
    class Meta:
        additional = ("registration_allowed")

class RegistrationState(db.Model, CRUDMixin):
    "This contains one row, which determines whether or not a new registration is allowed"
    __schema__ = RegistrationStateSchema
    id = db.Column(db.Integer(), primary_key=True)
    registration_allowed = db.Column(db.Boolean())
