from flask import Flask, request, jsonify
from flask_restx import Resource, Api

app = Flask("application")
api = Api(app)

from application.controllers import *

