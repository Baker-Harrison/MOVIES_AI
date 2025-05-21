from fastapi import FastAPI
from server.api.routes.movie import movie_router
from fastapi.middleware.cors import CORSMiddleware



def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(movie_router, prefix="/api/movie")

    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

    return app



app = create_app()



