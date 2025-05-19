from pydantic import BaseModel



class MovieWithId(BaseModel):
    id: int
    name: str
    rating: float
    plot: str


class MovieWithoutId(BaseModel):
    name: str
    rating: float
    plot: str