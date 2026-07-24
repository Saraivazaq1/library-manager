from sqlmodel import Session, delete, select
from ..models.autores import Autores


class AutorRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, autor: Autores) -> Autores:
        self._session.add(autor)
        self._session.commit()
        self._session.refresh(autor)
        return autor

    def get_autor_by_id(self, id: int) -> Autores:
        query = select(Autores).where(Autores.id == id)
        return self._session.exec(query).first()

    def get_autor_by_name(self, nome: str) -> list[Autores]:
        query = select(Autores).where(Autores.nome.ilike(f'%{nome}%'))
        return self._session.exec(query).all()

    def get_all(self) -> list[Autores]:
        query = select(Autores)
        return self._session.exec(query).all()

    def delete(self, autor: Autores):
        self._session.delete(autor)
        self._session.commit()

    def update(self, autor: Autores) -> Autores:
        self._session.add(autor)
        self._session.commit()
        self._session.refresh(autor)
        return autor