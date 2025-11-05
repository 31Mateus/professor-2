# int
# float
# str
# bool

idade = 16 #int
altura = 1.75 #float
nome = 'Mateus' #str
estudando = True #bool

# 1 Abstração
# reduzir para o que eu preciso
class Pessoa:
    def __init__(self,nome,altura,idade,peso):
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.peso = peso

# objeto da classe pessoa

p1 = Pessoa(nome="Mateus",altura=1.75,idade=16,peso="pena")

print(type(idade))
print(type(nome))

# class é o tipo do dado