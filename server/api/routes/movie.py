from fastapi import APIRouter, Depends, HTTPException
from fastapi.exceptions import ResponseValidationError
from sqlalchemy.orm import Session
from server.schemas.Movie import MovieWithoutId, MovieWithId
from server.api.deps import get_session
from server.models.Movie import Movie
from server.crud.models.movie import CRUDMOVIE
from pydantic import BaseModel, ValidationError

movie_router = APIRouter()
# /api/movie...


@movie_router.post('/add', response_model=MovieWithId)
def add_movie(movie: Movie, db: Session = Depends(get_session)):

    
    #db_movie = Movie (
    #    name=movie.name,
    #    rating=movie.rating,
    #    plot=movie.plot
    #)
    CRUDMOVIE.create(db, movie)

    return MovieWithId.model_validate(movie)

@movie_router.get('/get-all', response_model=list[MovieWithId])
async def get_all_movies(db: Session = Depends(get_session)):
    try:
        movies = CRUDMOVIE.get_all(db=db)
        return [MovieWithId.model_validate(movie) for movie in movies]
    except ValidationError as e:
        print(f"Error: {e}")


@movie_router.get('/{movie_name}', response_model=MovieWithId)
def get_movie_by_name(movie_name: str, db: Session = Depends(get_session)):
    db_movie = CRUDMOVIE.get_by_name(db, movie_name)
    if db_movie is None:
        raise HTTPException(
            status_code=404,
            detail=f"Movie with name '{movie_name}' not found"
        )
    return MovieWithId.model_validate(db_movie)