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
    
    if opcao ==  "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else: 
            print("Operação falhou! O valor informado é inválido.")    
            
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo 
        
        excedeu_limite = valor > limite 
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print()