#!/home/wligtenberg/.virtualenvs/closeness/bin/python
# -*- coding: utf-8 -*-
# closeness-server (c) Willem Ligtenberg

from closeness_server.wsgi import app
app.run(port=app.config['PORT'])
