Claro! Vou ajudá-lo a criar um sistema bancário simples em Python. Aqui está a implementação:

```python
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
```

Nesse código, a classe `Banco` representa a conta bancária com seus atributos, como saldo, número de saques realizados e histórico de transações. Ela possui os métodos `deposito`, `saque` e `extrato`, que realizam as operações conforme especificado.

A função `main` é responsável por exibir o menu e interagir com o usuário, chamando os métodos adequados da classe `Banco` com base na opção selecionada.

Para testar o sistema, execute a função `main` e siga as instruções exibidas no menu.

Lembrando que essa é apenas uma implementação simples para atender aos requisitos iniciais. Em um sistema real, seriam necessárias melhorias, como validações mais robustas, tratamento de erros e persistência dos dados em um banco de dados ou arquivo.