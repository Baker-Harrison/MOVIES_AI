from fastapi import FastAPI
from server.api.routes.movie import movie_router

app = FastAPI()


app.include_router(movie_router, prefix="/api/movie")


