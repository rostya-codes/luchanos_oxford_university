"""File with settings and config for the project"""
from email.policy import default

from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    'REAL_DATABASE_URL',
    default='postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres'
)  # connect string for the real database


ACCESS_TOKEN_EXPIRE_MINUTES: int = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)


TEST_DATABASE_URL = env.str(
    'REAL_DATABASE_URL',
    default='postgresql+asyncpg://postgres:postgres@0.0.0.0:5433/postgres_test'
)  # connect string for the test database

