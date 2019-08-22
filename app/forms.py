# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UrlForm(FlaskForm):
    original_url = StringField('Original Url', validators=[DataRequired()])
    submit = SubmitField('Shorten')
