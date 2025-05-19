# app/db/session.py

from sqlmodel import Session, create_engine, SQLModel
import os

# Create the database directory if it doesn't exist
DB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
os.makedirs(DB_DIR, exist_ok=True)

# Use absolute path for database file
SQLITE_FILE_NAME = os.path.join(DB_DIR, "dev.db")
SQLITE_URL = f"sqlite:///{SQLITE_FILE_NAME}"

engine = create_engine(
    SQLITE_URL,
    connect_args={"check_same_thread": False},
    echo=True
)

# Create a session factory instead of a single session
def get_session():
    with Session(engine) as session:
        yield session

# For direct session usage (like in init_db.py)
SessionLocal = Session(engine)




