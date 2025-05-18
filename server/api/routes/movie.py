from fastapi import APIRouter
from server.schemas.Movie import MovieWithoutId, MovieWithId


movie_router = APIRouter()




@movie_router.get('/{id}', response_model=MovieWithId)
def root(id: int):
    return {"id": id, "name": "test movie", "rating" : 10.8, "plot": "this is a test plot" }