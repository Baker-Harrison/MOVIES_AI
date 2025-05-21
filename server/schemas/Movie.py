from pydantic import BaseModel



class MovieWithId(BaseModel):
    id: int
    name: str
    rating: float
    plot: str
    model_config = {
        "from_attributes": True
    }

class MovieWithoutId(BaseModel):
    name: str
    rating: float
    plot: str
    model_config = {
        "from_attributes": True
    }