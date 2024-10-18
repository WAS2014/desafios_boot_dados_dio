from datetime import datetime

# Classe Cliente (somente Pessoa Física)
class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"

# Classe Historico para armazenar transações
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, tipo, valor):
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transacoes.append(f"{data_hora} - {tipo}: R${valor:.2f}")

    def listar_transacoes(self):
        print("Histórico de Transações:")
        for transacao in self.transacoes:
            print(transacao)

# Interface para transações (abstração)
class Transacao:
    def registrar(self, tipo, valor):
        raise NotImplementedError("Método deve ser implementado")

# Classe Conta Corrente
class Conta(Transacao):
    def __init__(self, numero, cliente, saldo_inicial=0.0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.historico = Historico()

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao("Depósito", valor)
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    # Método para sacar dinheiro da conta
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.adicionar_transacao("Saque", valor)
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    # Consulta o saldo da conta
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    # Método para listar o histórico de transações
    def listar_historico(self):
        self.historico.listar_transacoes()

    # Implementação do método registrar (herdado da interface Transacao)
    def registrar(self, tipo, valor):
        self.historico.adicionar_transacao(tipo, valor)

# Função principal (main)
def main():
    print("Bem-vindo ao Sistema Bancário")
    nome = input("Informe o nome do cliente: ")
    cpf = input("Informe o CPF do cliente: ")
    endereco = input("Informe o endereço do cliente: ")

    cliente = Cliente(nome, cpf, endereco)
    print(f"Cliente {cliente.nome} cadastrado com sucesso!")

    numero_conta = input("Informe o número da conta corrente: ")
    conta = Conta(numero_conta, cliente)
    print(f"Conta {numero_conta} criada com sucesso para o cliente {cliente.nome}.")

    while True:
        print("\n=== Operações Disponíveis ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Consultar Saldo")
        print("4. Histórico de Transações")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor para depósito: "))
            conta.depositar(valor)

        elif opcao == "2":
            valor = float(input("Informe o valor para saque: "))
            conta.sacar(valor)

        elif opcao == "3":
            conta.consultar_saldo()

        elif opcao == "4":
            conta.listar_historico()

        elif opcao == "5":
            print("Saindo do sistema bancário. Obrigado!")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
