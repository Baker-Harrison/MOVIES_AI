from server.db.session import SessionLocal



# For dependency injection
def get_session():
    with SessionLocal as session:
        yield session
