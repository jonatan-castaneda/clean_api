'''
Created on 26/12/2019

@author: Ian
'''

from paste.translogger import TransLogger
import cherrypy
from ston.config import webapp
from ston import app


def run_server():
    app_logged = TransLogger(webapp)
    cherrypy.tree.graft(app_logged, '/')
    cherrypy.config.update({
        'engine.autoreload.on': True,
        'log.screen': True,
        'server.socket_port': 5000,
        'server.socket_host': '0.0.0.0',
        "server.thread_pool": 50
    })
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    run_server()
