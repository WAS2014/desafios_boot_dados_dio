class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"


class ContaBancaria:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def transferir(self, destino, valor):
        if isinstance(destino, ContaBancaria) and 0 < valor <= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
            print(f"Transferência de R${valor:.2f} realizada para a conta {destino.numero}.")
        else:
            print("Transferência não realizada. Verifique o saldo ou o destino.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def __str__(self):
        return f"Conta número: {self.numero}, Cliente: {self.cliente.nome}, Saldo: R${self.saldo:.2f}"


class ContaCorrente(ContaBancaria):
    def __init__(self, numero, cliente, limite=1000.0):
        super().__init__(numero, cliente)
        self.limite = limite

    def sacar(self, valor):
        if 0 < valor <= (self.saldo + self.limite):
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso (com limite)!")
        else:
            print("Saldo insuficiente, mesmo com limite.")


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, cliente, rendimento=0.02):
        super().__init__(numero, cliente)
        self.rendimento = rendimento

    def aplicar_rendimento(self):
        self.saldo += self.saldo * self.rendimento
        print(f"Rendimento de {self.rendimento * 100:.2f}% aplicado. Novo saldo: R${self.saldo:.2f}")


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def criar_conta_corrente(self, cliente, numero):
        conta = ContaCorrente(numero, cliente)
        cliente.adicionar_conta(conta)
        self.contas.append(conta)

    def criar_conta_poupanca(self, cliente, numero):
        conta = ContaPoupanca(numero, cliente)
        cliente.adicionar_conta(conta)
        self.contas.append(conta)

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def listar_contas(self):
        for conta in self.contas:
            print(conta)


# Função para simular o sistema bancário
def main():
    banco = Banco("Banco Central")

    while True:
        print("\n===== Bem-vindo ao Banco Central =====")
        print("1. Adicionar Cliente")
        print("2. Criar Conta Corrente")
        print("3. Criar Conta Poupança")
        print("4. Listar Clientes")
        print("5. Listar Contas")
        print("6. Realizar Depósito")
        print("7. Realizar Saque")
        print("8. Transferir")
        print("9. Consultar Saldo")
        print("10. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Informe o nome do cliente: ")
            cpf = input("Informe o CPF do cliente: ")
            endereco = input("Informe o endereço do cliente: ")
            cliente = Cliente(nome, cpf, endereco)
            banco.adicionar_cliente(cliente)
            print(f"Cliente {nome} adicionado com sucesso!")

        elif opcao == "2":
            cpf = input("Informe o CPF do cliente para criar conta corrente: ")
            cliente = next((c for c in banco.clientes if c.cpf == cpf), None)
            if cliente:
                numero = int(input("Informe o número da conta corrente: "))
                banco.criar_conta_corrente(cliente, numero)
                print(f"Conta Corrente {numero} criada com sucesso para {cliente.nome}!")
            else:
                print("Cliente não encontrado.")

        elif opcao == "3":
            cpf = input("Informe o CPF do cliente para criar conta poupança: ")
            cliente = next((c for c in banco.clientes if c.cpf == cpf), None)
            if cliente:
                numero = int(input("Informe o número da conta poupança: "))
                banco.criar_conta_poupanca(cliente, numero)
                print(f"Conta Poupança {numero} criada com sucesso para {cliente.nome}!")
            else:
                print("Cliente não encontrado.")

        elif opcao == "4":
            print("\nLista de Clientes:")
            banco.listar_clientes()

        elif opcao == "5":
            print("\nLista de Contas:")
            banco.listar_contas()

        elif opcao == "6":
            numero = int(input("Informe o número da conta para depósito: "))
            conta = next((c for c in banco.contas if c.numero == numero), None)
            if conta:
                valor = float(input(f"Quanto deseja depositar na conta {numero}? "))
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "7":
            numero = int(input("Informe o número da conta para saque: "))
            conta = next((c for c in banco.contas if c.numero == numero), None)
            if conta:
                valor = float(input(f"Quanto deseja sacar da conta {numero}? "))
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "8":
            numero_origem = int(input("Informe o número da conta de origem: "))
            conta_origem = next((c for c in banco.contas if c.numero == numero_origem), None)
            if conta_origem:
                numero_destino = int(input("Informe o número da conta de destino: "))
                conta_destino = next((c for c in banco.contas if c.numero == numero_destino), None)
                if conta_destino:
                    valor = float(input(f"Quanto deseja transferir da conta {numero_origem} para a conta {numero_destino}? "))
                    conta_origem.transferir(conta_destino, valor)
                else:
                    print("Conta de destino não encontrada.")
            else:
                print("Conta de origem não encontrada.")

        elif opcao == "9":
            numero = int(input("Informe o número da conta para consultar saldo: "))
            conta = next((c for c in banco.contas if c.numero == numero), None)
            if conta:
                conta.consultar_saldo()
            else:
                print("Conta não encontrada.")

        elif opcao == "10":
            print("Saindo do sistema bancário. Até logo!")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
