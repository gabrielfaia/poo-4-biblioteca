import csv

class Usuario:
    def __init__(self, nome, id):
        self.nome = nome
        self._id = id

    def __str__(self):
        return f"{self.nome} (ID: {self._id})"
    

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        
    def exibir_livros(self):
        if not self.livros:
            return "Nenhum livro cadastrado na biblioteca!"
        else:
            lista = [f"- {livro}" for livro in self.livros]
            return f"Livros disponíveis:\n" + "\n".join(lista)
        
    def csv_livros(self):
        with open("livros.csv", mode="w", encoding="utf-8") as arquivo:
            if not self.livros:
                arquivo.write("Nenhum livro cadastrado.\n")
            else:
                for livro in self.livros:
                    if isinstance(livro, Livro):

                        arquivo.write(f"{livro.titulo} (Publicação: {livro.ano})\n")
                        arquivo.write(f"• Autor: {livro.autor}\n")
                        arquivo.write(f"• Páginas: {livro.paginas}\n\n")
        return f"[livros.csv] Os dados dos livros foram salvos!"

    def csv_usuarios(self):
        with open("usuarios.csv", mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Nome", "ID"])
            for usuario in self.usuarios:
                escritor.writerow([usuario.nome, usuario._id])
        return f"[usuarios.csv] Os dados dos usuários foram salvos!"


class Livro(Biblioteca):
    def __init__(self, titulo, autor, paginas, ano):
        super().__init__()
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano}), {self.paginas} páginas"


class Administrador(Usuario):
    def __init__(self, nome, id, biblioteca):
        super().__init__(nome, id)
        self.biblioteca = biblioteca

    def adicionar_usuario(self, usuario):
        self.biblioteca.usuarios.append(usuario)
        return f"Usuário {usuario.nome} adicionado com sucesso."
    
    def remover_usuario(self, id):
        for usuario in self.biblioteca.usuarios:
            if usuario._id == id:
                self.biblioteca.usuarios.remove(usuario)
                return f"Usuário {usuario.nome} removido com sucesso."
        return f"O usuário não foi encontrado."
    
    def adicionar_livro(self, livro):
        self.biblioteca.livros.append(livro)
        return f"Livro {livro} adicionado com sucesso."
    
    def remover_livro(self, livro):
        if livro in self.biblioteca.livros:
            self.biblioteca.livros.remove(livro)
            return f"Livro {livro} removido com sucesso."
        return f"O livro não foi encontrado."
