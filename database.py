from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite:///biblioteca.db", echo=False)


def criar_banco():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def nova_sessao():
    return Session(bind=engine)
