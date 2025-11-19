from datetime import datetime 
print()

class Conta:
    def __init__(self,numero_conta,titular):# Método construtor
        self.numero_conta = numero_conta
        self.titular = titular 
        self.saldo = 0
        self.data_criacao = datetime.now().date() 

class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
        self.cheque_especial = 400
    
    def sacar(self,valor_saque):
        if valor_saque < valor_saque:
            print("Saldo insuficiente")
            if self.saldo + self.cheque_especial < valor_saque:
                print("Cheque especial não cobre")
            else:
                self.saldo -= valor_saque
                print("Saque efetuado com sucesso! Cheque especial utilizado")
                
            return ""
        self.saldo -= valor_saque
        pass
    
    def depositar(self,valor_deposito):
        self.saldo += valor_deposito
        pass

    def transferir(self,conta_destinada:Conta):
        self.saldo -= 0
        conta_destinada.saldo += 100
        print("Transferência realizada com sucesso!")
        pass

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
    
    def gerar_juros(self):
        self.saldo += (1/100) * self.saldo
        pass


#conta1 = ContaCorrente("010203","Joao Pescador")
#print("SALDO ATUAL 1:",conta1.saldo)
#conta1.sacar(100)
#print("SALDO ATUAL 1:",conta1.saldo)
#print("="*30)
#conta1.depositar(100)
#print("SALDO ATUAL 1:",conta1.saldo)
#print("="*30)
#conta1.depositar(20)
#print("SALDO ATUAL 1:",conta1.saldo)
#print("="*30)
#conta2 = ContaCorrente("0405060","Mateus")
#print("SALDO ATUAL 2:",conta2.saldo)
#conta1.transferir(conta2)
#print("SALDO ATUAL 2:",conta2.saldo)
#print("SALDO ATUAL 1:",conta1.saldo)

contaPou = ContaPoupanca("010203","Gabriel")
contaPou.saldo = 1000
print("SALDO ATUAL POUPANÇA:",contaPou.saldo)
for i in range(30):
    contaPou.gerar_juros()
print("SALDO ATUAL POUPANÇA:",contaPou.saldo*12)

#contas = []
#while True:
    #print("1 - Adicionar Conta")
    #opcao = input("->")
    #if opcao == "1":
        #numero_conta = input("Digite o número da conta: ")
        #titular = input("Digite o nome do titular: ")
        #contas.append(Conta(numero_conta,titular))
        #break
    
#for i in contas:
    #print(vars(i))

#conta1 = Conta("010203","João papo de pescador")
#print(conta1.titular)
#print(conta1.numero_conta)