from biblioteca import Usuario, Biblioteca, Administrador, Livro

# Criação dos Usuários
usuario1 = Usuario("Gabriel", 11)
usuario2 = Usuario("Thiago", 12)
usuario3 = Usuario("Leonardo", 13)

# Criação da Biblioteca
biblioteca = Biblioteca()

# Criação do Administrador
admin = Administrador("Péricles", 1, biblioteca)

# Adição dos Livros (usando a nova classe Livro)
livro1 = Livro("Harry Potter: a Pedra Filosofal", "J.K. Rowling", 1997, 223)
livro2 = Livro("Star Wars: O Caminho Jedi", "Daniel Wallace", 2014, 160)
livro3 = Livro("Star Wars: A Ascensão Skywalker", "Rae Carson", 2020, 320)

print(admin.adicionar_livro(livro1))
print(admin.adicionar_livro(livro2))
print(admin.adicionar_livro(livro3))

# Exibição dos Livros
print("\n" + biblioteca.exibir_livros())

# Adição dos Usuários
print("\n" + admin.adicionar_usuario(usuario1))
print(admin.adicionar_usuario(usuario2))
print(admin.adicionar_usuario(usuario3))

# Tentativa de remover um usuário e livro que não existe
print("\n" + admin.remover_usuario(101))
print(admin.remover_livro("Qualquer livro"))

# Remoção de um livro existente
print("\n" + admin.remover_livro(livro3))

# Exibição dos livros após remoção
print("\n" + biblioteca.exibir_livros())

# Salvando os dados no CSV
print("\n" + biblioteca.csv_livros())
print(biblioteca.csv_usuarios())
