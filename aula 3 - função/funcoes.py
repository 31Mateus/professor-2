def definir_se_e_par(numero):
    resultado = ""
    if numero % 2 == 0:
        resultado = "Par"
    else:
        resultado = "Impar"
        
    return resultado
print(definir_se_e_par(5))
print(definir_se_e_par(6))
print(definir_se_e_par(7))
print(definir_se_e_par(8))
print(definir_se_e_par(9))
print(definir_se_e_par(10))