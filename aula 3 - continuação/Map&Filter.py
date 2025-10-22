print("SUCESSOR")

numeros = [1, 2, 3]
sucessor = list(map(lambda x: x+1,numeros))

print(sucessor)

print("="*30)
print("ANTECESSOR")

numeros = [1, 2, 3]
antecessor = list(map(lambda x: x-1,numeros))

print(antecessor)

print("="*30)
print("SUCESSOR DO QUINTUPLO")

numeros = [1, 2, 3]
sucessor_do_quintuplo = list(map(lambda x: x*5+1,numeros))

print(sucessor_do_quintuplo)

print("="*30)
print("NÚMEROS PARES")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2==0,numeros))

print(pares)

print("="*30)
print("NÚMEROS POSITIVOS")

numeros = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
positivos = list(filter(lambda x : x > 0 ,numeros))

print(positivos)

print("="*30)
print("NÚMEROS NEGATIVOS")

numeros = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
negativos = list(filter(lambda x : x < 0 ,numeros))

print(negativos)

print("="*30)
print("NÚMEROS ÍMPARES")

numeros = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = list(filter(lambda x : x %2 != 0 ,numeros))

print(impares)

print("="*30)
print("NÚMEROS MULTIPLOS")

numeros = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
multiplos_3_5 = list(filter(lambda x : x % 3 == 0 and x % 5 == 0 ,numeros))

print(multiplos_3_5)

print("="*30)

numeros = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
total = reduce(lambda acumulador,n : acumulador + n,numeros,0)
print(total)