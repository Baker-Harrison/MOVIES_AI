from fastapi import FastAPI
from .DataModels.Movie import Movie

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/movie", response_model=Movie)
async def movie(movie: Movie):



    
    return movie