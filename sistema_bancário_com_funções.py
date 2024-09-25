# Classe para o cliente (usuário)
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

# Classe para a conta bancária
class ContaBancaria:
    def __init__(self, cliente):
        self.cliente = cliente
        self.saldo = 0.0
        self.limite = 500.0
        self.limite_saques_diarios = 3
        self.saques_efetuados = 0
        self.extrato = []

# Função para cadastrar usuário
def cadastrar_usuario():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    return Cliente(nome, cpf)

# Função para cadastrar uma conta bancária
def cadastrar_conta(cliente):
    return ContaBancaria(cliente)

# Função para depositar
def depositar(conta, valor):
    if valor > 0:
        conta.saldo += valor
        conta.extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")

# Função para sacar
def sacar(conta, valor):
    if valor > 0:
        if conta.saques_efetuados >= conta.limite_saques_diarios:
            print("Limite diário de saques atingido!")
        elif valor > conta.limite:
            print(f"O valor de saque excede o limite de R$ {conta.limite:.2f}")
        elif conta.saldo + conta.limite >= valor:
            conta.saldo -= valor
            conta.extrato.append(f"Saque: R$ {valor:.2f}")
            conta.saques_efetuados += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente.")
    else:
        print("Valor de saque inválido.")

# Função para mostrar o extrato
def mostrar_extrato(conta):
    print(f"\nExtrato Bancário de {conta.cliente.nome}:")
    if not conta.extrato:
        print("Nenhuma transação realizada.")
    else:
        for transacao in conta.extrato:
            print(transacao)
    print(f"Saldo atual: R$ {conta.saldo:.2f}")
    print(f"Limite de crédito disponível: R$ {conta.limite + conta.saldo:.2f}")
    print(f"Saques restantes hoje: {conta.limite_saques_diarios - conta.saques_efetuados}\n")

# Função principal para o menu do banco
def main():
    print("Bem-vindo ao sistema bancário!")
    
    cliente = cadastrar_usuario()  # Cadastro do cliente
    conta = cadastrar_conta(cliente)  # Cadastro da conta bancária
    
    while True:
        print("\n--- Menu Banco ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Mostrar Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: R$ "))
            depositar(conta, valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: R$ "))
            sacar(conta, valor)
        elif opcao == '3':
            mostrar_extrato(conta)
        elif opcao == '4':
            print("Saindo do sistema. Obrigado por usar o banco!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()

