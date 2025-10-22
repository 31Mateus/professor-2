playlist = []
while True:
    print("="*30)
    print("PLAYLIST")
    print("="*30)
    print("1- Adicionar música")
    print("2- Retirar música")
    print("3- Listar Playlist")
    print("q - Sair")
    opcao = input("Digite sua opção:")
    
    if opcao == "1":
        música = input("Adicione uma música:")
        playlist.append(música)
        
    elif opcao == "2":
        deletar = input("Digite a música que deseja retirar:")
        playlist.remove(" ")
        
    elif opcao == "3":
        for i in playlist:
         print(i)
    elif opcao == "q":
        break
    else:
        print("Resposta Inválida")