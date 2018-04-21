from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PlexForm(FlaskForm):
    directory = StringField('Where is your Plex DVR directory?', validators=[DataRequired()])
    archivedir = StringField('Where is your Archive directory?', validators=[DataRequired()])
    submit = SubmitField('Submit')