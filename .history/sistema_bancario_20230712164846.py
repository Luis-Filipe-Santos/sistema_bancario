class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.saques_realizados = 0
        self.extrato = []

    def deposito(self, valor):
        if valor > 0.0:
            self.saldo += valor
            self.extrato.append(f'Depósito: +R${valor:.2f}')
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Valor inválido para depósito.')

    def saque(self, valor):
        if self.saques_realizados < 3:
            if 0 < valor <= 500.0:
                if valor <= self.saldo:
                    self.saldo -= valor
                    self.saques_realizados += 1
                    self.extrato.append(f'Saque: -R${valor:.2f}')
                    print(f'Saque de R${valor:.2f} realizado com sucesso.')
                else:
                    print('Saldo insuficiente para realizar o saque.')
            else:
                print('Valor inválido para saque (limite é de R$500.00).')
        else:
            print('Você já atingiu o limite diário de saques.')

    def extrato(self):
        for movimento in self.extrato:
            print(movimento)
        print(f'Saldo atual: R${self.saldo:.2f}')


def main():
    banco = Banco()

    while True:
        print('\n===== MENU =====')
        print('Opções: (d)Depósito, (s)Saque, (e)Extrato, (q)Sair')
        opcao = input('Selecione uma opção: ')

        if opcao == 'd':
            valor = float(input('Digite o valor a ser depositado: '))
            banco.deposito(valor)
        elif opcao == 's':
            valor = float(input('Digite o valor a ser sacado: '))
            banco.saque(valor)
        elif opcao == 'e':
            banco.extrato()
        elif opcao == 'q':
            break
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()
