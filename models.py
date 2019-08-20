from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from settings.config import PG_CONN


db = SQLAlchemy(**PG_CONN)


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(8))
    
    date_created = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return f"{self.original_url!r}: {self.short_url!r}"
