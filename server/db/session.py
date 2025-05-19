# app/db/session.py

from sqlmodel import Session, create_engine, SQLModel


SQLITE_FILE_NAME = "dev.db"
SQLITE_URL = f"sqlite:///{SQLITE_FILE_NAME}"

engine = create_engine(
    SQLITE_URL,
    connect_args={"check_same_thread": False},
    echo=True
)

SessionLocal = Session(engine)

# For dependency injection
def get_session():
    with SessionLocal as session:
        yield session
    

