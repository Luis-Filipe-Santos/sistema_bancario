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

    def deposito(self, saldo, valor, *, extrato):
        if valor > 0.0:
            saldo += valor
            extrato.append(f'Depósito: +R${valor:.2f}')
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Valor inválido para depósito.')

        return saldo, extrato

    def saque(self, *, saldo, limite, extrato):
        if len(extrato) < 3:
            valor = float(input('Digite o valor a ser sacado: '))

            if 0 < valor <= limite:
                if valor <= saldo:
                    saldo -= valor
                    extrato.append(f'Saque: -R${valor:.2f}')
                    print(f'Saque de R${valor:.2f} realizado com sucesso.')
                else:
                    print('Saldo insuficiente para realizar o saque.')
            else:
                print('Valor inválido para saque (limite é de R$500.00).')
        else:
            print('Você já atingiu o limite diário de saques.')

        return saldo, extrato

    def extrato(self, saldo, *, extrato):
        for movimento in extrato:
            print(movimento)
        print(f'Saldo atual: R${saldo:.2f}')


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


def main():
    lista_usuarios = []
    lista_contas = []

    while True:
        print('\n===== MENU =====')
        print('Opções: (d)Depósito, (s)aque, (e)xtrato, (c)riar usuário, (v)incular conta, (q)uit')
        opcao = input('Selecione uma opção: ')

        if opcao == 'd':
            saldo = float(input('Digite o saldo da conta: '))
            valor = float(input('Digite o valor a ser depositado: '))
            saldo, extrato = deposito(saldo, valor, extrato=[])
            print(f'Saldo atual: R${saldo:.2f}')
        elif opcao == 's':
            saldo = float(input('Digite o saldo da conta: '))
            limite = 500.0
            extrato = []
            saldo, extrato = saque(saldo=saldo, limite=limite, extrato=extrato)
            print(f'Saldo atual: R${saldo:.2f}')
        elif opcao == 'e':
            saldo = float(input('Digite o saldo da conta: '))
            extrato = []
            extrato(saldo, extrato=extrato)
        elif opcao == 'c':
            usuario = criar_cliente()
            lista_usuarios.append(usuario)
            print('Usuário criado com sucesso.')
        elif opcao == 'v':
            vincular_conta_corrente(lista_contas, lista_usuarios)
        elif opcao == 'q':
            break
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()
