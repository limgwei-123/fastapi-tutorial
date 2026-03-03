from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRESQL_USER = "postgres"
POSTGRESQL_PASSWORD="limgwei000"
POSTGRESQL_HOST = "localhost"
POSTGRESQL_PORT = "5432"
POSTGRESQL_DATABASE="fastapi_db"

DATABASE_URL = f'postgresql+psycopg://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_DATABASE}'

## Conection
engine = create_engine(DATABASE_URL)

## Session
SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind= engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

## Base
Base = declarative_base()