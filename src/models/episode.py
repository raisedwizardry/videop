from flask_restplus import fields
from server.instance import server


episode = server.api.model('Episode', {
    'episodesign': fields.String(required=True, min_length=6, max_length=20, description='Episode in S00E00'),
    'title': fields.String(description='Episode title'),
    'show': fields.String(required=True, description='Show title')
})
