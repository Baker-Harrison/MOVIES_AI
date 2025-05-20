from fastapi import FastAPI
from server.api.routes.movie import movie_router



def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(movie_router, prefix="/api/movie")
    


    return app



app = create_app()



