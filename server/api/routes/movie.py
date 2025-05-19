from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from server.schemas.Movie import MovieWithoutId, MovieWithId
from server.api.deps import get_session
from server.models.Movie import Movie

movie_router = APIRouter()

@movie_router.get('/', response_model=MovieWithId)
def root( db: Session = Depends(get_session)):
    first_movie = db.query(Movie).first()
    return first_movie