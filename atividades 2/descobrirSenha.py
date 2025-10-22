def descobridor_de_senhas(senha):
    contador = 0
    while True:
        senha_gerada = ""
        for i in range(4):
            senha_gerada += str(random.randint(0,9))
        contador +=1
        print(senha_gerada)
        print(senha)
        
        if senha_gerada == senha:
            print(f"Você acertou! A senha é {senha_gerada}")
            print(f"O número de tentativas foi:{contador}")
            break
    print(contador)
        
    print(descobridor_de_senhas("4258"))