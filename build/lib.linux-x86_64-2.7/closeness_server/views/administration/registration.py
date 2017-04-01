# -*- coding: utf-8 -*-
# closeness-server (c) Willem Ligtenberg

from flask_security import ConfirmRegisterForm
from flask_wtf.recaptcha import RecaptchaField


class ExtendedRegisterForm(ConfirmRegisterForm):
    recaptcha = RecaptchaField()

    def validate(self):
        rv = ConfirmRegisterForm.validate(self)
        if not rv:
            return False

        return True
