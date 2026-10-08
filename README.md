# Atividade Prática 02 - Consultas e Operações em uma Biblioteca Persistente
## André Nícolas de Oliveira Santos

## Respostas:

1. Para que serve o campo `disponivel`?
   Ele controla se um livro pode ser emprestado naquele momento, quando o valor é `True`, o livro está disponível, quando é `False` ele está indisponível.

2. Por que usar `session.commit()`?
   Porque a alteração feita no objeto do banco precisa ser salva de forma persistente, sem `commit()`, a mudança fica apenas na sessão e não é gravada no banco.

3. Onde você usa o relacionamento Livro`` - `Autor`?
   Em `listar_livros`, onde cada livro acessa `livro.autor.nome` para mostrar o nome do autor, e em `listar_livros_por_autor`, quando o autor é buscado e depois seus livros são percorridos por `autor.livros`.
