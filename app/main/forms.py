from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    directory = StringField('Where is your Plex DVR directory?', validators=[DataRequired()])
    time = StringField('What time do you want to Process?', validators=[DataRequired()])
    submit = SubmitField('Submit')
