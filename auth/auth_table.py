from auth.auth_database import engine, Base
from auth import models

# syntax use to create db
Base.metadata.create_all(bind=engine)