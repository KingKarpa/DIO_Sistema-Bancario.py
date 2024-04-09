menu = """
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

=> """

saldo = 0
saques_realizados = 0
extrato = ""
# Quantidade máxima de operações de saque diárias
MAX_DIARIO_SAQUE = 3
# Valor máximo de saque por operação
MAX_VALOR_SAQUE = 500

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor de depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! Valor informado é inválido.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_valor_limite = valor > MAX_VALOR_SAQUE
        excedeu_saque_diario = saques_realizados >= MAX_DIARIO_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_valor_limite:
            print("Operação falhou! O valor de saque excedeu o limite (R$ 500,00).")
        
        elif excedeu_saque_diario:
            print("Operação falhou! Número máximo de saques diários excedido.")

        elif valor > 0:
            saldo -= valor
            saques_realizados += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! Valor informado é inválido.")
    
    elif opcao == "3":
        print("======= EXTRATO =======")
        print("Nenhuma movimentação foi realizada na conta hoje." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================")
    
    elif opcao == "4":
        break

    else:
        print("Operação falhou! Opção informada não existe, tente novamente.")