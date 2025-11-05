class Carro:
    def __init__(self,cor,modelo,ano): # Método construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        
    def acelerar(self):
        self.velocidade += 8
        return f"O carro {self.modelo} acelerou para {self.velocidade} km/h"

    def frear(self):
        self.velocidade -= 3
        return f"O carro {self.modelo} freou para {self.velocidade} km/h"
    
c1 = Carro(
        cor = input("Cor do carro: "),
        modelo = input("Modelo do carro: "),
        ano = int(input("Ano do carro: "))
    )

c1 = Carro(cor="prata",modelo="celta",ano=2003)

print(Carro.acelerar(c1))
print(Carro.acelerar(c1))
print(Carro.acelerar(c1))
print(Carro.acelerar(c1))
print(Carro.frear(c1))
print(Carro.frear(c1))
print(Carro.frear(c1))
print(Carro.frear(c1))
print(Carro.frear(c1))
