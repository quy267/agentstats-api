# -*- coding: utf-8 -*-
from flask_pymongo import PyMongo
from flask_oauth2.resources import ResourceProvider
from flask_oauth2.clients import Oauth2Client
from flask_permissions import permissions
from webargs.flaskparser import FlaskParser

resource = ResourceProvider()
mongo = PyMongo()
oauth2 = Oauth2Client()
perms = permissions.Permissions()
parser = FlaskParser()
