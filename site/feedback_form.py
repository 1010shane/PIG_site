from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, validators
from wtforms.validators import DataRequired

class FeedbackForm(FlaskForm):
    satisfaction = RadioField('Satisfaction', choices = [0, 1, 2, 3, 4, 5], validators = [DataRequired()])
