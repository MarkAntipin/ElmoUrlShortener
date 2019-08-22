# -*- coding: utf-8 -*-

from app import app
from app.handlers import manage

manage.register(app)

if __name__ == '__main__':
    app.run()
