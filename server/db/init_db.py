# app/db/init_db.py

from sqlmodel import SQLModel
from server.db.session import engine, SessionLocal
from server.models.Movie import Movie

def init_db():
    # Create tables
    SQLModel.metadata.create_all(bind=engine)
    
    

if __name__ == "__main__":
    init_db()