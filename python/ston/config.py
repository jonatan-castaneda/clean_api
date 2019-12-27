'''
Created on 26/12/2019

@author: Ian
'''
from flask.app import Flask
import os 

env = os.getenv("ENV", "DEV")
webapp = Flask(__name__)
webapp.config['DEBUG'] = True
path = os.getcwd()
cache_path = "{}/ston/cache".format(path)