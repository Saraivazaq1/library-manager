from sqlmodel import Field, SQLModel

class Usuarios(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=255, index=True)
    email: str = Field(max_length=255, index=True, nullable=False, unique=True)