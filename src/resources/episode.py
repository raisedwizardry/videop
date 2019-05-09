from flask import Flask
from flask_restplus import Api, Resource, fields

from server.instance import server
from models.episode import episode

app, api = server.app, server.api

# Let's just keep them in memory
episode_db = [
    {"id": 0, "episodesign": "S02E19", "title": "The Chicken Fight", "show": "Family Guy"},
    {"id": 1, "episodesign": "S01E12", "title": "Robin in the Hood", "show": "Bob's Burgers"},
]

@api.route('/api/episodes')
class EpisodeList(Resource):
    @api.marshal_list_with(episode)
    def get(self):
        return episode_db

@api.route('/api/episodes/<int:id>')
class Episode(Resource):
    # Utility method
    def find_one(self, id):
        return next((b for b in episode_db if b["id"] == id), None)

    @api.marshal_with(episode)
    def get(self, id):
        match = self.find_one(id)
        return match if match else ("Not found", 404)
