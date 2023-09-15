from sqlmodel import Field, SQLModel, Date


class Pessoa(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    apelido: str = Field(max_length=32, unique=True)
    nome: str = Field(max_length=100)
    nascimento: str = Date()
    stack: list[str] | None = Field(default=None)
