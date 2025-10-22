notas = []
while True:
    print("1 - adicione um novo aluno")
    print("2 - sair")
    opcao = input("Digite sua opção:")
    dicionario = {}
    if opcao == "1":
        dicionario['nome'] = input("nome do aluno:")
        dicionario['nota'] = input("nota do aluno:")
        notas.append(dicionario)
    if opcao == "2":
        break