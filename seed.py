from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    if session.query(Livro).first() is not None:
        return

    autor1 = Autor(nome="Machado de Assis", pais="Brasil")
    autor2 = Autor(nome="George Orwell", pais="Reino Unido")
    autor3 = Autor(nome="Jane Austen", pais="Reino Unido")

    session.add(autor1)
    session.add_all([autor2, autor3])
    session.flush()

    livros = [
        Livro(titulo="Memórias Póstumas de Brás Cubas", ano=1881, autor=autor1, disponivel=True),
        Livro(titulo="Dom Casmurro", ano=1899, autor=autor1, disponivel=False),
        Livro(titulo="1984", ano=1949, autor=autor2, disponivel=True),
        Livro(titulo="A Revolução dos Bichos", ano=1945, autor=autor2, disponivel=False),
        Livro(titulo="Orgulho e Preconceito", ano=1813, autor=autor3, disponivel=True),
        Livro(titulo="Persuasão", ano=1817, autor=autor3, disponivel=True),
    ]

    session.add_all(livros)
    session.commit()
