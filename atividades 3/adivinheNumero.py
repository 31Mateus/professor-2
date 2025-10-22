print("="*30)
print("ADIVINHE O NÚMERO".center(30))
print("="*30)
from random import randint

aleatorio = randint(1, 10)

while True:
    numero = int(input("Digite um número entre 1 e 10: "))
    if numero == aleatorio:
        print("Parabéns! Você adivinhou o número.")
        break
    else:
        print('Errado! Tente novamente.')
    if numero > aleatorio:
            print('Menos')
    else:
            print('Mais')