from sqlmodel import SQLModel, Field


class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    cost: int


class EditTransaction(SQLModel):
    name: str | None = None
    cost: int | None = None


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    hashed_password: str
    is_active: bool = Field(default=True)
