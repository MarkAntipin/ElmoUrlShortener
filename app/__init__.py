from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from settings.config import PG_CONN
from settings.paths import BASE_DIR

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     f"postgresql://{PG_CONN['user']}:{PG_CONN['password']}"
#     f"@{PG_CONN['host']}/{PG_CONN['database']}"
# )


app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///' + Path(BASE_DIR, 'elmo-url.db').as_posix()
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)
