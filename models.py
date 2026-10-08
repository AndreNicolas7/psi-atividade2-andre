from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    pais: Mapped[str]

    livros: Mapped[List["Livro"]] = relationship(back_populates="autor")


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    ano: Mapped[int]
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))
    disponivel: Mapped[bool] = mapped_column(default=True)

    autor: Mapped["Autor"] = relationship(back_populates="livros")
