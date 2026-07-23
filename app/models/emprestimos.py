from datetime import date, timedelta

from sqlmodel import CheckConstraint, Field, SQLModel


class Emprestimos(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    id_usuario: int | None = Field(default=None, foreign_key="usuarios.id")
    id_livro: int | None = Field(default=None, foreign_key="livros.id")

    data_emprestimo: date = Field(default_factory=lambda: date.today())
    data_devolucao: date = Field(
        default_factory=lambda: date.today() + timedelta(days=14)
    )

    status: str = Field(
        default="Emprestado",
        max_length=20,
        sa_column_kwargs={"server_default": "Emprestado"},
    )

    __table_args__ = (
        CheckConstraint(
            "status IN ('Emprestado', 'Devolvido')",
            name="chk_emprestimos_status"
        ),
    )