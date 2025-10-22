import random
def gerar_senha(tamanho):
    lista_caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    aleatorio = random.choice(lista_caracteres,)
    senha_gerada = ""
    for i in range(tamanho):
        senha_gerada += random.choice(lista_caracteres)
        
    return senha_gerada

print(gerar_senha(8))