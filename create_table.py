from database import engine, Base
import model

# syntax use to create db
Base.metadata.create_all(bind=engine)