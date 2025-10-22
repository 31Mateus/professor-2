numero = int(input("digite um número para fazer o fatorial:"))
for i in range(numero, 1, -1):
    numero = numero*i
    print(numero)