menu = """

[d] Depositar
[s] Sacar
[t] Transferir
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito concluído com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente para realizar o saque.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque concluído com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "t":

        while True:

            agencia = input("Insira o número da agência para qual deseja transferir um valor (4 dígitos): ")
            
            if agencia.isnumeric() and len(agencia) == 4:
                agencia = int(agencia)  
                break  
            else:
                print("Número de agência inválido! É necessário ter 4 dígitos no total.")

        while True:

            conta = input("Insira o número da conta para qual deseja transferir um valor (5 dígitos): ")
            
            if conta.isnumeric() and len(conta) == 5:
                conta = int(conta)  
                break
            else:
                print("Número de conta inválido! É necessário ter 5 dígitos no total.")

        while True:

            valor = float(input("Informe o valor da transferência: "))
            
            excedeu_saldo = valor > saldo

            if excedeu_saldo:
             print("Operação falhou! Você não tem saldo suficiente para realizar a transferência.")

            elif valor <= 0:
                print("Operação falhou! É necessário realizar transferências acima de R$ 0.00.")

            else:
                saldo -= valor
                extrato += f"Transferir: R$ {valor:.2f}\n"
                print("Transferência concluída com sucesso!")
                break

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
