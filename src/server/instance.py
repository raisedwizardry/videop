from flask import Flask
from flask_restplus import Api, Resource, fields
from server.environment import environment_config


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version='1.0',
                       title='videop',
                       description='A simple transcoding api',
                       doc=environment_config["swagger-url"]
                       )

    def run(self):
        self.app.run(
            debug=environment_config["debug"],
            port=environment_config["port"]
        )


server = Server()
