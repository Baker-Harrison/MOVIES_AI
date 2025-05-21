from server.crud.base import CRUDBase
from server.models.Movie import Movie
from sqlmodel import Session

class CRUDMovie(CRUDBase[Movie]):
    # Add movie-specific methods here
    def get_by_name(self, db: Session, name: str) -> Movie | None:
        return db.query(self.model).filter(self.model.name == name).first()
    


# Create an instance to use in routes
CRUDMOVIE = CRUDMovie(Movie)