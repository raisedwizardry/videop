from flask import Flask
from flask_restplus import Api, Resource, fields

from server.instance import server
from models.episode import episode

app, api = server.app, server.api

# Let's just keep them in memory
episode_db = [
    {"episodesign": "S02E19", "title": "The Chicken Fight", "show": "Family Guy"},
    {"episodesign": "S01E12", "title": "Robin in the Hood", "show": "Bob's Burgers"},
]

@api.route('/episodes')
class EpisodeList(Resource):
    @api.marshal_list_with(episode)
    def get(self):
        return episode_db
