from app import app
from app.handlers import manage
from settings.config import PG_CONN


manage.register(app)

if __name__ == '__main__':
    app.run()
