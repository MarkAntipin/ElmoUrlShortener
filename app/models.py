# -*- coding: utf-8 -*-
import string
from random import choices
from datetime import datetime

from flask_migrate import Migrate

from app import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(6), unique=True)
    
    date_created = db.Column(db.DateTime(), default=datetime.now())
    
    def __init__(self, original_url, **kwargs):
        super().__init__(**kwargs)
        self.original_url = original_url
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        charecters = string.digits + string.ascii_letters
        short_url = ''.join(choices(charecters, k=6))

        url = self.query.filter_by(short_url=short_url).first()
        if url:
            return url

        return short_url

    def __repr__(self):
        return f"({self.original_url!r}: {self.short_url!r})"


if __name__ == '__main__':
    db.create_all()