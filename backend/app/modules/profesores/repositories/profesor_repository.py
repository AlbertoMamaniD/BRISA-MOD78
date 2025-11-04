from sqlalchemy.orm import Session
from app.modules.profesores.models.profesor_models import Profesor,Materia, Curso

class ProfesorRepository:

    @staticmethod
    def create(db: Session, profesor: dict) -> Profesor:
        nuevo_profesor = Profesor(**profesor)
        db.add(nuevo_profesor)
        db.commit()
        db.refresh(nuevo_profesor)
        return nuevo_profesor

    @staticmethod
    def get_all(db: Session):
        return db.query(Profesor).all()

    @staticmethod
    def get_by_id(db: Session, id_persona: int):
        return db.query(Profesor).filter(Profesor.id_persona == id_persona).first()

    @staticmethod
    def update(db: Session, profesor: Profesor, data: dict):
        for key, value in data.items():
            setattr(profesor, key, value)
        db.commit()
        db.refresh(profesor)
        if profesor.id_cargo:
            db.refresh(profesor.cargo) 
        return profesor

    @staticmethod
    def delete(db: Session, profesor: Profesor):
        db.delete(profesor)
        db.commit()
        return profesor

class MateriaRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(Materia).all()

class CursoRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(Curso).all()