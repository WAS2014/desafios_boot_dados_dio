class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.limite = 500.0
        self.limite_saques_diarios = 3
        self.saques_efetuados = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0:
            if self.saques_efetuados >= self.limite_saques_diarios:
                print("Limite diário de saques atingido!")
            elif valor > self.limite:
                print(f"O valor de saque excede o limite de R$ {self.limite:.2f}")
            elif self.saldo + self.limite >= valor:
                self.saldo -= valor
                self.extrato.append(f"Saque: R$ {valor:.2f}")
                self.saques_efetuados += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor de saque inválido.")

    def mostrar_extrato(self):
        print("\nExtrato Bancário:")
        if not self.extrato:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.extrato:
                print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"Limite de crédito disponível: R$ {self.limite + self.saldo:.2f}")
        print(f"Saques restantes hoje: {self.limite_saques_diarios - self.saques_efetuados}\n")

    def sair(self):
        print("Saindo do sistema. Obrigado por usar o banco!")

def main():
    conta = Banco()
    
    while True:
        print("\n--- Menu Banco ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Mostrar Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: R$ "))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: R$ "))
            conta.sacar(valor)
        elif opcao == '3':
            conta.mostrar_extrato()
        elif opcao == '4':
            conta.sair()
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
