from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from settings.config import PG_CONN, SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{PG_CONN['user']}:{PG_CONN['password']}"
    f"@{PG_CONN['host']}/{PG_CONN['database']}"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)
