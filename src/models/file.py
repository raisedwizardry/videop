from flask_restplus import fields
from server.instance import server

file = server.api.model('File', {
    'file': fields.String(),
})