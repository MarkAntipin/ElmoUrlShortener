from app import app
from app.handlers import manage

manage_image.register(app)

if __name__ == '__main__':
    app.run()
