import csv
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

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
        
    def reservar_livro(self, livro, usuario):
        return f"Livro '{livro.titulo}' reservado para {usuario.nome}!"

    # Procura livros por título ou autor
    def procurar_livro(self, termo):
        resultados = []
        termo_lower = termo.lower()
        for livro in self.livros:
            if termo_lower in livro.titulo.lower() or termo_lower in livro.autor.lower():
                resultados.append(livro)
        return resultados

    def csv_livros(self):
        with open("livros.csv", mode="w", encoding="utf-8") as arquivo:
            if not self.livros:
                arquivo.write("Nenhum livro cadastrado.\n")
            else:
                for livro in self.livros:
                    if isinstance(livro, Livro):
                        arquivo.write(f"{livro.titulo};{livro.ano};{livro.autor};{livro.paginas}\n")

        return f"[livros.csv] Os dados dos livros foram salvos!"

    def csv_usuarios(self):
        with open("usuarios.csv", mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Nome", "ID"])
            for usuario in self.usuarios:
                escritor.writerow([usuario.nome, usuario._id])
        return f"[usuarios.csv] Os dados dos usuários foram salvos!"


class Livro:
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
    
class BibliotecaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")
        self.root.geometry("500x700")
        self.root.resizable(False, False)

        # Inicializar o sistema
        self.biblioteca = Biblioteca()
        self.admin = Administrador("Admin", "001", self.biblioteca)

        # Adicionar alguns dados de exemplo
        self.dados_exemplo()

        # Título
        titulo = tk.Label(root, text="Sistema de Biblioteca",
                          font=("Arial", 20, "bold"), pady=20)
        titulo.pack()

        # Frame principal para os botões
        frame_botoes = tk.Frame(root)
        frame_botoes.pack(pady=10, padx=20, fill='both', expand=True)

        # === Botões Principais === #
        # Botão: Procurar Livro
        btn_procurar = tk.Button(frame_botoes, text="Procurar Livro",
                                 command=self.procurar_livro,
                                 font=("Arial", 12), bg="#4CAF50", fg="white",
                                 height=2, relief='raised', bd=3)
        btn_procurar.pack(fill='x', pady=5)

        # Botão: Reservar Livro
        btn_reservar = tk.Button(frame_botoes, text="Reservar Livro",
                                 command=self.reservar_livro,
                                 font=("Arial", 12), bg="#2196F3", fg="white",
                                 height=2, relief='raised', bd=3)
        btn_reservar.pack(fill='x', pady=5)

        # Separador
        ttk.Separator(frame_botoes, orient='horizontal').pack(fill='x', pady=15)

        # === Botões dos Módulos ===
        label_modulos = tk.Label(frame_botoes, text="Módulos do Sistema:",
                                 font=("Arial", 11, "bold"))
        label_modulos.pack(pady=(5, 10))

        # Botão: Adicionar Livro
        btn_add_livro = tk.Button(frame_botoes, text="Adicionar Livro",
                                  command=self.adicionar_livro,
                                  font=("Arial", 10), bg="#FF9800", fg="white",
                                  height=2, relief='raised', bd=2)
        btn_add_livro.pack(fill='x', pady=3)

        # Botão: Remover Livro
        btn_rem_livro = tk.Button(frame_botoes, text="Remover Livro",
                                  command=self.remover_livro,
                                  font=("Arial", 10), bg="#F44336", fg="white",
                                  height=2, relief='raised', bd=2)
        btn_rem_livro.pack(fill='x', pady=3)

        # Botão: Adicionar Usuário
        btn_add_usuario = tk.Button(frame_botoes, text="Adicionar Usuário",
                                    command=self.adicionar_usuario,
                                    font=("Arial", 10), bg="#9C27B0", fg="white",
                                    height=2, relief='raised', bd=2)
        btn_add_usuario.pack(fill='x', pady=3)

        # Botão: Remover Usuário
        btn_rem_usuario = tk.Button(frame_botoes, text="Remover Usuário",
                                    command=self.remover_usuario,
                                    font=("Arial", 10), bg="#E91E63", fg="white",
                                    height=2, relief='raised', bd=2)
        btn_rem_usuario.pack(fill='x', pady=3)

        # Botão: Exibir Livros
        btn_exibir = tk.Button(frame_botoes, text="Exibir Todos os Livros",
                               command=self.exibir_livros,
                               font=("Arial", 10), bg="#607D8B", fg="white",
                               height=2, relief='raised', bd=2)
        btn_exibir.pack(fill='x', pady=3)

        # Separador
        ttk.Separator(frame_botoes, orient='horizontal').pack(fill='x', pady=10)

        # Botão: Exportar CSV Livros
        btn_csv_livros = tk.Button(frame_botoes, text="Exportar Livros (CSV)",
                                   command=self.exportar_livros,
                                   font=("Arial", 10), bg="#00BCD4", fg="white",
                                   height=2, relief='raised', bd=2)
        btn_csv_livros.pack(fill='x', pady=3)

        # Botão: Exportar CSV Usuários
        btn_csv_usuarios = tk.Button(frame_botoes, text="Exportar Usuários (CSV)",
                                    command=self.exportar_usuarios,
                                    font=("Arial", 10), bg="#009688", fg="white",
                                    height=2, relief='raised', bd=2)
        btn_csv_usuarios.pack(fill='x', pady=3)

    # Dados (livros) de exemplo pós-inicialização do programa
    def dados_exemplo(self):
        livro1 = Livro("Dom Casmurro", "Machado de Assis", 256, 1899)
        livro2 = Livro("1984", "George Orwell", 328, 1949)
        livro3 = Livro("O Cortiço", "Aluísio Azevedo", 232, 1890)

        self.admin.adicionar_livro(livro1)
        self.admin.adicionar_livro(livro2)
        self.admin.adicionar_livro(livro3)

        usuario1 = Usuario("Gabriel", "1")
        usuario2 = Usuario("Thiago", "2")
        usuario3 = Usuario("Leonardo", "3")

        self.admin.adicionar_usuario(usuario1)
        self.admin.adicionar_usuario(usuario2)
        self.admin.adicionar_usuario(usuario3)

    # === Métodos que chamam os Módulos das Classes ===
    def procurar_livro(self):
        termo = tk.simpledialog.askstring("Procurar Livro",
                                       "Digite o título ou autor do livro:")
        if termo:
            resultados = self.biblioteca.procurar_livro(termo)
            if resultados:
                texto = "Livros encontrados:\n\n"
                for livro in resultados:
                    texto += f"• {livro}\n"
                messagebox.showinfo("Resultados da Busca", texto)
            else:
                messagebox.showinfo("Resultados da Busca",
                                    "Nenhum livro encontrado com esse termo.")

    def reservar_livro(self):
        if not self.biblioteca.livros:
            messagebox.showwarning("Atenção", "Nenhum livro disponível para reserva!")
            return

        if not self.biblioteca.usuarios:
            messagebox.showwarning("Atenção", "Nenhum usuário cadastrado!")
            return

        # Janela para seleção
        janela = tk.Toplevel(self.root)
        janela.title("Reservar Livro")
        janela.geometry("400x300")

        tk.Label(janela, text="Selecione o livro:", font=("Arial", 10, "bold")).pack(pady=5)

        var_livro = tk.StringVar()
        combo_livro = ttk.Combobox(janela, textvariable=var_livro,
                                   values=[str(l) for l in self.biblioteca.livros],
                                   state='readonly', width=50)
        combo_livro.pack(pady=5)

        tk.Label(janela, text="Selecione o usuário:", font=("Arial", 10, "bold")).pack(pady=5)

        var_usuario = tk.StringVar()
        combo_usuario = ttk.Combobox(janela, textvariable=var_usuario,
                                     values=[str(u) for u in self.biblioteca.usuarios],
                                     state='readonly', width=50)
        combo_usuario.pack(pady=5)

        def confirmar_reserva():
            if var_livro.get() and var_usuario.get():
                idx_livro = combo_livro.current()
                idx_usuario = combo_usuario.current()

                livro = self.biblioteca.livros[idx_livro]
                usuario = self.biblioteca.usuarios[idx_usuario]

                mensagem = self.biblioteca.reservar_livro(livro, usuario)
                messagebox.showinfo("Sucesso", mensagem)
                janela.destroy()
            else:
                messagebox.showwarning("Atenção", "Selecione livro e usuário!")

        tk.Button(janela, text="Confirmar Reserva", command=confirmar_reserva,
                  bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

    def adicionar_livro(self):
        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Livro")
        janela.geometry("350x250")

        tk.Label(janela, text="Título:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        entry_titulo = tk.Entry(janela, width=30)
        entry_titulo.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(janela, text="Autor:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        entry_autor = tk.Entry(janela, width=30)
        entry_autor.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(janela, text="Páginas:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        entry_paginas = tk.Entry(janela, width=30)
        entry_paginas.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(janela, text="Ano:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
        entry_ano = tk.Entry(janela, width=30)
        entry_ano.grid(row=3, column=1, padx=10, pady=5)

        def salvar():
            try:
                livro = Livro(entry_titulo.get(), entry_autor.get(),
                              int(entry_paginas.get()), int(entry_ano.get()))
                mensagem = self.admin.adicionar_livro(livro)
                messagebox.showinfo("Sucesso", mensagem)
                janela.destroy()
            except ValueError:
                messagebox.showerror("Erro", "Páginas e Ano devem ser números!")

        tk.Button(janela, text="Salvar", command=salvar, bg="#4CAF50",
                  fg="white").grid(row=4, column=0, columnspan=2, pady=15)

    def remover_livro(self):
        if not self.biblioteca.livros:
            messagebox.showwarning("Atenção", "Nenhum livro cadastrado!")
            return

        janela = tk.Toplevel(self.root)
        janela.title("Remover Livro")
        janela.geometry("500x200")

        tk.Label(janela, text="Selecione o livro para remover:",
                 font=("Arial", 10, "bold")).pack(pady=10)

        var = tk.StringVar()
        combo = ttk.Combobox(janela, textvariable=var,
                             values=[str(l) for l in self.biblioteca.livros],
                             state='readonly', width=60)
        combo.pack(pady=10)

        def confirmar():
            if var.get():
                idx = combo.current()
                livro = self.biblioteca.livros[idx]
                mensagem = self.admin.remover_livro(livro)
                messagebox.showinfo("Sucesso", mensagem)
                janela.destroy()

        tk.Button(janela, text="Remover", command=confirmar, bg="#F44336",
                  fg="white", font=("Arial", 10, "bold")).pack(pady=10)

    def adicionar_usuario(self):
        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Usuário")
        janela.geometry("300x150")

        tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        entry_nome = tk.Entry(janela, width=25)
        entry_nome.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(janela, text="ID:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
        entry_id = tk.Entry(janela, width=25)
        entry_id.grid(row=1, column=1, padx=10, pady=10)

        def salvar():
            usuario = Usuario(entry_nome.get(), entry_id.get())
            mensagem = self.admin.adicionar_usuario(usuario)
            messagebox.showinfo("Sucesso", mensagem)
            janela.destroy()

        tk.Button(janela, text="Salvar", command=salvar, bg="#9C27B0",
                  fg="white").grid(row=2, column=0, columnspan=2, pady=10)

    def remover_usuario(self):
        if not self.biblioteca.usuarios:
            messagebox.showwarning("Atenção", "Nenhum usuário cadastrado!")
            return

        janela = tk.Toplevel(self.root)
        janela.title("Remover Usuário")
        janela.geometry("400x200")

        tk.Label(janela, text="Selecione o usuário para remover:",
                 font=("Arial", 10, "bold")).pack(pady=10)

        var = tk.StringVar()
        combo = ttk.Combobox(janela, textvariable=var,
                             values=[str(u) for u in self.biblioteca.usuarios],
                             state='readonly', width=50)
        combo.pack(pady=10)

        def confirmar():
            if var.get():
                idx = combo.current()
                usuario_id = self.biblioteca.usuarios[idx]._id
                mensagem = self.admin.remover_usuario(usuario_id)
                messagebox.showinfo("Sucesso", mensagem)
                janela.destroy()

        tk.Button(janela, text="Remover", command=confirmar, bg="#E91E63",
                  fg="white", font=("Arial", 10, "bold")).pack(pady=10)

    def exibir_livros(self):
        mensagem = self.biblioteca.exibir_livros()
        messagebox.showinfo("Livros Cadastrados", mensagem)

    def exportar_livros(self):
        mensagem = self.biblioteca.csv_livros()
        messagebox.showinfo("Exportar", mensagem)

    def exportar_usuarios(self):
        mensagem = self.biblioteca.csv_usuarios()
        messagebox.showinfo("Exportar", mensagem)
