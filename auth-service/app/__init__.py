from os import environ
from sqlalchemy.ext import declarative
from sqlalchemy import ext
from sqlalchemy import orm
import logging
import dotenv
import asyncio

dotenv.load_dotenv('./.env')

SERVICE_NAME = environ.get('SERVICE_NAME')

PREFIX = environ.get('PREFIX', default='/api')
TESTING = (environ.get('TESTING', default='false') == 'true')

DATABASE_URL = 'sqlite+aiosqlite://{}:{}@{}:{}/{}'.format(
    environ.get('DB_USER', default='root'),
    environ.get('DB_PASSWORD', default=''),
    environ.get('DB_HOST', default='localhost'),
    environ.get('DB_PORT', default='3306'),
    environ.get('DB_MAIN', default='main') if not TESTING
    else environ.get('DB_TEST', default='test'),
)

OPENAPI_URL = '{}/{}/openapi.json'.format(PREFIX, SERVICE_NAME)
DOCS_URL = '{}/{}/docs'.format(PREFIX, SERVICE_NAME)

engine = ext.asyncio.create_async_engine(DATABASE_URL)
base = declarative.declarative_base()
session = orm.sessionmaker(
    bind=engine,
    class_=ext.asyncio.AsyncSession,
    expire_on_commit=False
)

logger = logging.getLogger(__name__)
