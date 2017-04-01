# -*- coding: utf-8 -*-
# closeness-server (c) Willem Ligtenberg

from ..models import Role, User


def typical_workflow():
    "create some example objects"

    Role.add_default_roles()

    User.register(
        email="guest@example.com",
        password="guest",
        roles=["User"],
    )

    User.register(
        email="admin@example.com",
        password="viu",
        roles=["Admin"],
    )
