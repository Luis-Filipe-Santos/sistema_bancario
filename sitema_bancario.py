class Banco:
    def __init__(self):
        self.saldo = 0
        self.saques_realizados = 0
        self.historico = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f'Depósito: R${valor:.2f}')
        else:
            print("O valor do depósito deve ser positivo.")

    def saque(self, valor):
        if self.saques_realizados < 3 and valor <= 500 and valor <= self.saldo:
            self.saldo -= valor
            self.saques_realizados += 1
            self.historico.append(f'Saque: R${valor:.2f}')
        elif self.saques_realizados >= 3:
            print("Você já realizou o número máximo de saques diários.")
        elif valor > 500:
            print("O valor do saque não pode ser maior que R$500.00.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def extrato(self):
        print("Histórico de transações:")
        for transacao in self.historico:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")


# Função principal
def main():
    banco = Banco()

    while True:
        print("\n----- Menu -----")
        print("Opções: (d)epósito, (s)aque, (e)xtrato, (q)uit")
        opcao = input("Selecione uma opção: ")

        if opcao == "d":
            valor = float(input("Digite o valor do depósito: "))
            banco.deposito(valor)
        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))
            banco.saque(valor)
        elif opcao == "e":
            banco.extrato()
        elif opcao == "q":
            break
        else:
            print("Opção inválida. Tente novamente.")


# Execução do programa
if __name__ == "__main__":
    main()
