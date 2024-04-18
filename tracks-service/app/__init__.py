from os import environ
import logging
import dotenv
import base_library

dotenv.load_dotenv('./.env')

SERVICE_NAME = environ.get('SERVICE_NAME')

PREFIX = environ.get('PREFIX', default='/api')
TESTING = (environ.get('TESTING', default='false') == 'true')

DATABASE_URL = 'postgresql+asyncpg://{}:{}@{}:{}/{}'.format(
    environ.get('DB_USER', default='root'),
    environ.get('DB_PASSWORD', default=''),
    environ.get('DB_HOST', default='localhost'),
    environ.get('DB_PORT', default='3306'),
    environ.get('DB_MAIN', default='main') if not TESTING
    else environ.get('DB_TEST', default='test'),
)

OPENAPI_URL = '{}/{}/openapi.json'.format(PREFIX, SERVICE_NAME)
DOCS_URL = '{}/{}/docs'.format(PREFIX, SERVICE_NAME)

engine, session = base_library.database.init_connection(DATABASE_URL)
logger = logging.getLogger(__name__)
