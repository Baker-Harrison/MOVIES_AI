from typing import Generic, Type, TypeVar
from sqlmodel import Session, SQLModel, select

ModelType = TypeVar("ModelType", bound=SQLModel)

class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int) -> ModelType | None:
        return db.get(self.model, id)

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> list[ModelType]:
        statement = select(self.model).offset(skip).limit(limit)
        return db.exec(statement).all()

    def create(self, db: Session, obj_in: ModelType) -> ModelType:
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def delete(self, db: Session, id: int) -> ModelType | None:
        obj = db.get(self.model, id)
        if obj:
            db.delete(obj)
            db.commit()
        return obj