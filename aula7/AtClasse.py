class Cachorro:
    def __init__(self,nome,cor,raca,caracteristicas):
        self.nome = nome
        self.cor = cor
        self.raca = raca
        self.caracteristicas = caracteristicas
        
p1 = Cachorro(nome="Catarina",cor="Preto",raca="Lhasa",caracteristicas="Fofa")

print(type(p1.nome))
print(type(p1.cor))

print("="*30)

class Pessoa:
    def __init__(self,nome,altura,idade,peso):
       self.nome = nome
       self.altura = altura
       self.idade = idade
       self.peso = peso

p2 = Pessoa(nome="Mateus",altura=1.75,idade=16,peso="pena")

print(type(p2.nome))
print(type(p2.idade))

print("="*30)

class Carro:
    def __init__(self,cor,modelo,ano): # Método construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        
c1 = Carro(cor="prata",modelo="celta",ano=2003)
print(c1.cor)
print(vars(c1))
