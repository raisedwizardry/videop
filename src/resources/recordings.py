from flask import Flask
from flask_restplus import Api, Resource, fields

from server.instance import server
from data.recordings import DirectoryFiles
from server.environment import video_file_path

app, api = server.app, server.api

@api.route('/api/recordings')
class FileList(Resource):
    def get(self):
        return DirectoryFiles(video_file_path).files
