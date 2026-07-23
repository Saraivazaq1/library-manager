from sqlmodel import Field, SQLModel

class Livros(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str = Field(max_length=255, index=True, nullable=False)
    id_autor: int | None = Field(default=None, foreign_key="autores.id")
    id_categoria: int | None = Field(default=None, foreign_key="categorias.id")