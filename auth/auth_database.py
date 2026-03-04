from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

POSTGRESQL_USER = os.getenv("POSTGRESQL_USER", "postgres")
POSTGRESQL_PASSWORD= os.getenv("POSTGRESQL_PASSWORD", "limgwei000")
POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST", "db")
POSTGRESQL_PORT = os.getenv("POSTGRESQL_PORT", "5432")
POSTGRESQL_DATABASE= os.getenv("POSTGRESQL_DATABASE", "fastapi_db")

DATABASE_URL = f'postgresql+psycopg://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_DATABASE}'

## Conection
engine = create_engine(DATABASE_URL,
                       echo= True,
                       pool_pre_ping= True)

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