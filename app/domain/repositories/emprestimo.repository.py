from sqlmodel import Session, select

from app.domain.models.emprestimos import Emprestimos


class EmprestimoRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, emprestimo: Emprestimos):
        self._session.add(emprestimo)
        self._session.commit()
        self._session.refresh(emprestimo)
        return emprestimo

    def get_emprestimo_by_id(self, id: int) -> Emprestimos:
        query = select(Emprestimos).where(Emprestimos.id == id)
        return self._session.exec(query).first

    def get_emprestimo_by_usuario(self, id_usuario: int) -> list[Emprestimos]:
        query = select(Emprestimos).where(Emprestimos.id_usuario == id_usuario)
        return self._session.exec(query).all()

    def get_all(self) -> list[Emprestimos]:
        query = select(Emprestimos)
        return self._session.exec(query).all()

    def delete(self, emprestimo: Emprestimos):
        self._session.delete(emprestimo)
        self._session.commit()

    def update(self, emprestimo: Emprestimos) -> Emprestimos:
        self._session.add(emprestimo)
        self._session.commit()
        self._session.refresh(emprestimo)
        return emprestimo
