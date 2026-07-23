from sqlmodel import Field, SQLModel

class Autores(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=255, index=True, nullable=False)