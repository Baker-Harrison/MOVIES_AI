from pydantic import BaseModel

class Movie(BaseModel):
    movie_name: str
    total_rating: float