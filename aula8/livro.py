class Biblioteca:
    def __init__(self):
        self.catalogo_livros = []
        self.lista_membros = []
        

class Editora:
        def __init__(self,nome,email):
            self.nome = nome
            self.email = email
            
class Autor:
        def __init__(self,nome,data_nascimento):
            self.nome = nome
            self.data_nascimento = data_nascimento           

class Livro:
        def __init__(self,titulo,anoPub,editora: Editora, autor: Autor):
            self.titulo = titulo
            self.anoPub = anoPub
            self.editora = editora
            self.autor = autor

a1 = Autor(nome="MEGA Siqueira",data_nascimento="14/02/1999")
ed1 = Editora("Clash Royale","royaleclash@clash.com")
l1 = Livro("Como parar de ser noob no Clash",2025,ed1,a1)

print("Nome do livro:", l1.titulo)
print("Ano de publicação:", l1.anoPub)
print("Nome da editora:", l1.editora.nome)
print("Email da editora:", l1.editora.email)
print("Nome do autor:", l1.autor.nome)
print("Data de nascimento do autor:", l1.autor.data_nascimento)
