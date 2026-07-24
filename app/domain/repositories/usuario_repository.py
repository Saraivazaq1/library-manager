from sqlmodel import Session, select

from app.domain.models.usuarios import Usuarios


class UsuarioRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, usuario: Usuarios) -> Usuarios:
        self._session.add(usuario)
        self._session.commit()
        self._session.refresh(usuario)
        return usuario

    def get_usuario_by_id(self, id: int) -> Usuarios:
        query = select(Usuarios).where(Usuarios.id == id)
        return self._session.exec(query).first()

    def get_usuario_by_email(self, email: str) -> Usuarios:
        query = select(Usuarios).where(Usuarios.email == email)
        return self._session.exec(query).first()

    def get_all(self) -> list[Usuarios]:
        query = select(Usuarios)
        return self._session.exec(query).all()

    def delete(self, usuario: Usuarios):
        self._session.delete(usuario)
        self._session.commit()

    def update(self, usuario: Usuarios) -> Usuarios:
        self._session.add(usuario)
        self._session.commit()
        self._session.refresh(usuario)
        return usuario