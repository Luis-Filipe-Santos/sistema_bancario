menu =  """" 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3 

while True: 
    
    opcao = input(menu)
    
    if opcao ==  "d"
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"