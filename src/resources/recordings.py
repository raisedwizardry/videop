from flask import Flask, request
from flask_restplus import Api, Resource, fields

from server.instance import server
from data.recordings import DirectoryFiles, Filename
from server.environment import video_file_path
from models.filedetail import filedetail
from models.file import file

app, api = server.app, server.api

@api.route('/api/recordings')
class FileList(Resource):
    @api.marshal_with(file)
    def get(self):
        return DirectoryFiles(video_file_path).files

@api.route('/api/recordings/detail')
class FileDetail(Resource):
    @api.marshal_with(filedetail)
    def get(self):
        filepath = request.args['file']
        return Filename(filepath)
    
    @api.expect(file)   
    @api.marshal_with(filedetail)
    def post(self):
        payload_data = request.get_json(force=True)
        filepath = payload_data.get("file")
        return Filename(filepath)