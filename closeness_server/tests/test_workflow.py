# -*- coding: utf-8 -*-
# closeness-server (c) Willem Ligtenberg

from nose.plugins.attrib import attr
from ..models import User
from .mixins import DiamondTestCase
from .fixtures import typical_workflow


class WorkflowTestCase(DiamondTestCase):
    def setUp(self):
        super(WorkflowTestCase, self).setUp()
        typical_workflow()

    @attr("single")
    def test_user(self):
        "user created in workflow"
        u = User.find(email='guest@example.com')
        assert u
        assert u.email == 'guest@example.com'
