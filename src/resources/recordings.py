from flask import Flask
from flask_restplus import Api, Resource, fields

from server.instance import server
from data.directory import files

app, api = server.app, server.api

@api.route('/api/recordings')
class FileList(Resource):
    def get(self):
        return files.listDirectoryTs()
