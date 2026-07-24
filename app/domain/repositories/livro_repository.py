from sqlmodel import Session, select

from app.domain.models.livros import Livros


class LivroRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, livro: Livros) -> Livros:
        self._session.add(livro)
        self._session.commit()
        self._session.refresh()
        return livro

    def get_livro_by_id(self, id: int) -> Livros:
        query = select(Livros).where(Livros.id == id)
        return self._session.exec(query).first()

    def get_livro_by_id(self, titulo: str) -> list[Livros]:
        query = select(Livros).where(Livros.titulo == titulo)
        return self._session.exec(query).all()

    def get_all(self) -> list[Livros]:
        query = select(Livros)
        return self._session.exec(query).all()

    def delete(self, livro: Livros):
        self._session.delete(livro)
        self._session.commit()

    def update(self, livro: Livros) -> Livros:
        self._session.add(livro)
        self._session.commit()
        self._session.refresh()
        return livro