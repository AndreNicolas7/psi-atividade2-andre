from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    livros = session.execute(select(Livro).order_by(Livro.titulo)).scalars().all()

    if not livros:
        print("Nenhum livro cadastrado.")
        return livros

    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"- {livro.titulo} | Autor: {livro.autor.nome} | Status: {status}")

    return livros


def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    livros = session.execute(
        select(Livro).where(Livro.disponivel.is_(True)).order_by(Livro.titulo)
    ).scalars().all()

    if not livros:
        print("Nenhum livro disponível.")
        return livros

    for livro in livros:
        print(f"- {livro.titulo} | Autor: {livro.autor.nome}")

    return livros


def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    livros = session.execute(
        select(Livro).where(Livro.titulo.ilike(f"%{trecho}%")).order_by(Livro.titulo)
    ).scalars().all()

    if not livros:
        print(f"Nenhum livro encontrado com o trecho '{trecho}'.")
        return livros

    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"- {livro.titulo} | Autor: {livro.autor.nome} | Status: {status}")

    return livros


def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    autor = session.scalar(select(Autor).where(Autor.nome.ilike(f"%{nome_autor}%")))

    if autor is None:
        print(f"Autor '{nome_autor}' não encontrado.")
        return []

    livros = sorted(autor.livros, key=lambda livro: livro.titulo)

    if not livros:
        print(f"Nenhum livro encontrado para o autor '{autor.nome}'.")
        return livros

    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"- {livro.titulo} | Status: {status}")

    return livros
