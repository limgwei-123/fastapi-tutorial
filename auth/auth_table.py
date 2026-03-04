from auth_database import engine, Base
import models

# syntax use to create db
Base.metadata.create_all(bind=engine)