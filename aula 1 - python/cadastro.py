usuarios = []
while True:
    print("="*30)
    print("Cadastro de usuários")
    print("="*30)
    print("1- Cadastrar usuário")
    print("2- Atualizar Usuário")
    print("3- Deletar Usuário")
    print("4- Listar Usuário")
    print("q - Sair")
    opcao = input("Digite sua opção:")
    
    if opcao == "1":
        nome = input("Digite seu nome:")
        usuarios.append(nome)

    elif opcao == "2":
        atualizar = input("Digite o nome de usuário que deseja atualizar:")
        atualizar = []
        
    elif opcao == "3":
        deletar = input("Digite o nome de usuário que deseja deletar:")
        usuarios.remove("deletar")
        
    elif opcao == "4":
        for i in usuarios:
         print(i)
    elif opcao == "q":
        break
    else:
        print("Resposta Inválida")