def multiplicar_array(L):
    resultado = 1
    for n in L:
        resultado *= n
    return resultado
L = [1,2,3,4]
print(multiplicar_array(L))