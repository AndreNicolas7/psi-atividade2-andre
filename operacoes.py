from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    """Marque um livro como indisponível."""
    livro = session.scalar(select(Livro).where(Livro.titulo.ilike(f"%{titulo}%")))

    if livro is None:
        print(f"Livro '{titulo}' não encontrado.")
        return None

    if not livro.disponivel:
        print(f"Livro '{livro.titulo}' já está indisponível.")
        return livro

    livro.disponivel = False
    session.commit()
    print(f"Livro '{livro.titulo}' foi emprestado com sucesso.")
    return livro


def devolver_livro(session, titulo):
    """Marque um livro como disponível."""
    livro = session.scalar(select(Livro).where(Livro.titulo.ilike(f"%{titulo}%")))

    if livro is None:
        print(f"Livro '{titulo}' não encontrado.")
        return None

    if livro.disponivel:
        print(f"Livro '{livro.titulo}' já está disponível.")
        return livro

    livro.disponivel = True
    session.commit()
    print(f"Livro '{livro.titulo}' foi devolvido com sucesso.")
    return livro
