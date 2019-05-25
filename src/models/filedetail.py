from flask_restplus import fields
from server.instance import server

filedetail = server.api.model('Detail', {
    'fullFilename': fields.String(),
    'fullPath': fields.String(),
    'extention': fields.String(),
    'seInfo': fields.String(),
    'seasonNumber': fields.Integer(),
    'episodeNumber': fields.Integer(),
    'title': fields.String(),
    'show': fields.String(),
    'movieTitle': fields.String(),
    'movieYear': fields.String(),
    'isMovie': fields.Boolean()
})
