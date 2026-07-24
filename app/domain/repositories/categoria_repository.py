from sqlmodel import Session, select

from app.domain.models.categorias import Categorias


class CategoriaRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, categoria: Categorias) -> Categorias:
        self._session.add(categoria)
        self._session.commit()
        self._session.refresh(categoria)
        return categoria

    def get_categoria_by_id(self, id: int) -> Categorias:
        query = select(Categorias).where(Categorias.id == id)
        return self._session.exec(query).first

    def get_categoria_by_categoria(self, categoria: str) -> Categorias:
        query = select(Categorias).where(Categorias.categoria == categoria)
        return self._session.exec(query).first

    def get_all(self) -> list[Categorias]:
        query = select(Categorias)
        return self._session.exec(query).all()

    def delete(self, categoria: Categorias):
        self._session.delete(categoria)
        self._session.commit()

    def update(self, categoria: Categorias) -> Categorias:
        self._session.add(categoria)
        self._session.commit()
        self._session.refresh(categoria)
        return categoria
