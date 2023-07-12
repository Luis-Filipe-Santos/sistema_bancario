# ----------------- funções
class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


class ContaCorrente:
    def __init__(self, agencia, numero_conta, cliente):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0.0
        self.extrato = []

    def deposito(self, valor, *, extrato):
        if valor > 0.0:
            self.saldo += valor
            extrato.append(f'Depósito: +R${valor:.2f}')
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Valor inválido para depósito.')

        return self.saldo, extrato

    def saque(self, limite, *, extrato):
        if len(extrato) < 3:
            valor = float(input('Digite o valor a ser sacado: '))

            if 0 < valor <= limite:
                if valor <= self.saldo:
                    self.saldo -= valor
                    extrato.append(f'Saque: -R${valor:.2f}')
                    print(f'Saque de R${valor:.2f} realizado com sucesso.')
                else:
                    print('Saldo insuficiente para realizar o saque.')
            else:
                print('Valor inválido para saque (limite é de R$500.00).')
        else:
            print('Você já atingiu o limite diário de saques.')

        return self.saldo, extrato

    def imprimir_extrato(self, *, extrato):
        print('Extrato:')
        for movimento in extrato[-5:]:
            print(movimento)
        print(f'Saldo atual: R${self.saldo:.2f}')


def criar_cliente():
    nome = input('Nome: ')
    data_nascimento = input('Data de Nascimento (dd/mm/aaaa): ')
    cpf = input('CPF: ')
    endereco = input('Endereço: ')

    return Cliente(nome, data_nascimento, cpf, endereco)


def criar_conta_corrente(agencia, numero_conta, cliente):
    return ContaCorrente(agencia, numero_conta, cliente)


def vincular_conta_corrente(lista_contas, lista_usuarios):
    cpf = input('Digite o CPF do cliente: ')

    for usuario in lista_usuarios:
        if usuario.cpf == cpf:
            numero_conta = len(lista_contas) + 1
            conta = criar_conta_corrente('0001', numero_conta, usuario)
            lista_contas.append(conta)
            print(f'Conta corrente número {numero_conta} vinculada ao cliente {usuario.nome}.')
            break
    else:
        print('CPF não encontrado.')


def visualizar_clientes(lista_contas):
    for conta in lista_contas:
        cliente = conta.cliente
        print(f'Nome: {cliente.nome}')
        print(f'Data de Nascimento: {cliente.data_nascimento}')
        print(f'CPF: {cliente.cpf}')
        print(f'Endereço: {cliente.endereco}')
        print(f'Agência: {conta.agencia}')
        print(f'Número da Conta: {conta.numero_conta}')
        print(f'Saldo: R${conta.saldo:.2f}')
        print('---')


def main():
    lista_usuarios = []
    lista_contas = []
    
# ----------------- Menu
    while True:
        print('\n===== MENU =====')
        print('Opções: (d)Depósito, (s)Saque, (e)Extrato, (v)Visualizar clientes, (c)Criar usuário, (a)Associar conta, (q)SAIR')
        opcao = input('Selecione uma opção: ')

        if opcao == 'd':
            valor = float(input('Digite o valor a ser depositado: '))
            conta_numero = int(input('Digite o número da conta: '))

            for index, conta in enumerate(lista_contas):
                if conta.numero_conta == conta_numero:
                    saldo, extrato = conta.deposito(valor, extrato=[])
                    print(f'Saldo atual: R${saldo:.2f}')
                    break
            else:
                print('Conta não encontrada.')

        elif opcao == 's':
            limite = 500.0
            conta_numero = int(input('Digite o número da conta: '))

            for index, conta in enumerate(lista_contas):
                if conta.numero_conta == conta_numero:
                    extrato = []
                    saldo, extrato = conta.saque(limite=limite, extrato=extrato)
                    print(f'Saldo atual: R${saldo:.2f}')
                    break
            else:
                print('Conta não encontrada.')

        elif opcao == 'e':
            conta_numero = int(input('Digite o número da conta: '))

            for index, conta in enumerate(lista_contas):
                if conta.numero_conta == conta_numero:
                    extrato = []
                    conta.imprimir_extrato(extrato=conta.extrato)
                    break
            else:
                print('Conta não encontrada.')

        elif opcao == 'v':
            visualizar_clientes(lista_contas)

        elif opcao == 'c':
            usuario = criar_cliente()
            lista_usuarios.append(usuario)
            print('Usuário criado com sucesso.')

        elif opcao == 'a':
            vincular_conta_corrente(lista_contas, lista_usuarios)

        elif opcao == 'q':
            break

        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()
