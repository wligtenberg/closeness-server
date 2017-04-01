from flask_diamond import db
from flask_diamond.mixins.crud import CRUDMixin

class Registation_state(db.Model, CRUDMixin):
    "This contains one row, which determines whether or not a new registration is allowed"
    registration_allowed = db.Column(db.Boolean())
