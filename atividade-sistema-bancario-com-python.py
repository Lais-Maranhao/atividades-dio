menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Insira o valor a ser depositado na conta: "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito no valor de: {valor:.2f}") 
        else:
            print("O valor informado é inválido. Favor inserir um valor positivo para depósito")
    
    elif opcao == "s":
        valor = float(input("Insira o valor para saque: "))

        if valor > saldo:
            print(f"Não há saldo suficiente para saque. Favor inserir um valor menor ou igual a R$ {saldo:.2f}")
        elif valor > limite:
            print("Valor maior que o limite de saque. Favor inserir um valor menor ou igual a R$ 500.00")
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite diário de saques atingido.")
        
        elif valor > 0 and valor < saldo and valor <= limite:
            saldo -= valor
            extrato.append(f"Saque no valor de: {valor:.2f}")
            numero_saques += 1

        else:
            print("Operação inválida. O valor informado não é válido para saque")
    
    elif opcao == "e":
        print("**********EXTRATO**********")
        for item in extrato:
            print(item)
        print(f"Saldo da conta: R$ {saldo:.2f}")
        print("************FIM************")
    
    elif opcao == "q":
        break

    else:
        print("Opção digitada é inválida. Favor escolher uma opção válida.")
