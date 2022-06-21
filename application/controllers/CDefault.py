from application import api
from flask import *
from flask_restx import *

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}