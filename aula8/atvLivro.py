class Biblioteca:
    def __init__(self):
        self.catalogo_livros = []
        self.lista_membros = []
        
    class Biblioteca:
    def __init__(self):
        self.catalogo_livros = []
        self.lista_membros = []
        
    def emprestar_livro(self, livro, membro):
        if livro in self.catalogo_livros and membro in self.lista_membros:
            self.catalogo_livros.remove(livro)
            print(f"Livro '{livro.titulo}' emprestado para {membro.nome}.")
        else:
            print("Empréstimo não disponível.")

    def devolver_livro(self, livro, membro):
        self.catalogo_livros.append(livro)
        print(f"Livro '{livro.titulo}' devolvido por {membro.nome}.")
        
    def adicionar_novo_livro(self, livro):
        self.catalogo_livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado ao catálogo.")
        
    def adicionar_novo_membro(self, membro):
        self.lista_membros.append(membro)
        print(f"Membro '{membro.nome}' adicionado à biblioteca.")
    
class Livro:
    def __init__(self,titulo,anoPub,editora, autor):
        self.titulo = titulo
        self.anoPub = anoPub
        self.editora = editora
        self.autor = autor 
        
class Membro:
    def __init__(self,nome,numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro