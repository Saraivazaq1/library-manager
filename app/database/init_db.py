from sqlmodel import SQLModel
from .connection import engine
from ..models.usuarios import Usuarios
from ..models.autores import Autores
from ..models.emprestimos import Emprestimos
from ..models.livros import Livros
from ..models.categorias import Categorias


def init_db():
    SQLModel.metadata.create_all(engine)