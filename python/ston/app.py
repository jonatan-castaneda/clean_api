'''
Created on 24/08/2019

@author: Gera e Ian
'''
from flask_restful import Api
from flask_cors.extension import CORS
from ston.config import webapp
from flask import jsonify
from ston.main.Main import Main

api = Api(webapp)
CORS(webapp, resources={r"/*": {"origins": "*"}})

# Mailer
api.add_resource(Main, '/v1/main/<string:option>')