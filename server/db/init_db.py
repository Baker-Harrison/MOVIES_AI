# app/db/init_db.py

from sqlmodel import SQLModel
from server.db.session import engine, SessionLocal
from server.models.Movie import Movie

def init_db():
    # Create tables
    SQLModel.metadata.create_all(bind=engine)
    
    session = SessionLocal
    try:
        new_movie = Movie(
            name="Example Movie",
            rating=9.8,
            plot="Example Plot"
        )

        session.add(new_movie)

        session.commit()
    
        session.refresh(new_movie)
    finally:
        session.close()

if __name__ == "__main__":
    init_db()