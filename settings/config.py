import os
import dotenv

from settings.paths import BASE_DIR

dotenv.load_dotenv(
    os.path.join(BASE_DIR, 'settings', 'env')
)

PG_CONN = {
    'host': os.environ.get('PG_HOST', 'localhost'),
    'user': os.environ['PG_USER'],
    'password': os.environ['PG_PASSWORD'],
    'database': os.environ['PG_DATABASE'],
}
PG_DATABASE = os.environ['PG_DATABASE']
