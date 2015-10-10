# -*- coding: utf-8 -*- 
#!flask/bin/python
# manage.py

from flask.ext.script import Manager
from flask import Flask

from libs.unisender import Unisender

import json

app = Flask(__name__)
manager = Manager(app)


@manager.command
def subscribe():
    api = Unisender('api key')
    data = {'fields[email]': 'exmaple@example.com', 'list_ids': 100}
    print api.run('subscribe', data)

if __name__ == "__main__":
    manager.run()
