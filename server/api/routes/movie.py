from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from server.schemas.Movie import MovieWithoutId, MovieWithId
from server.api.deps import get_session
from server.models.Movie import Movie
from server.crud.models.movie import CRUDMOVIE

movie_router = APIRouter()

@movie_router.get('/{movie_name}', response_model=MovieWithId)
def get_movie_by_name(movie_name: str, db: Session = Depends(get_session)):
    db_movie = CRUDMOVIE.get_by_name(db, movie_name)
    return db_movie

@movie_router.post('/create', response_model=MovieWithId)
def add_movie(movie: Movie, db: Session = Depends(get_session)):

    
    db_movie = Movie (
        name=movie.name,
        rating=movie.rating,
        plot=movie.plot
    )

    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

    return db_movie