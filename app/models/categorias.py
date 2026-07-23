from sqlmodel import Field, SQLModel

class Categorias(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    categoria: str = Field(max_length=255, index=True, nullable=False)