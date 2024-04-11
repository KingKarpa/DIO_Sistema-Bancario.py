def menu():
    return input("""
    =============== MENU ===============
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Nova Conta
    [5] - Listar Contas
    [6] - Novo Usuário
    [7] - Sair

    => """)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        
    else:
        print("Operação falhou! Valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, saques_realizados, MAX_DIARIO_SAQUE, MAX_VALOR_SAQUE):
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
    
    return saldo, extrato, saques_realizados

def exibir_extrato(saldo, /, *, extrato):
    print("\n======= EXTRATO =======")
    print("Nenhuma movimentação foi realizada na conta hoje." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=======================")

def criar_usuario(usuarios):
    cpf = input("\nDigite seu CPF (apenas números): ")
    
    if buscar_usuario(usuarios, cpf):
        print("Operação falhou! Já existe um usuário com esse CPF.")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço: (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nDigite seu CPF (apenas números): ")
    usuario = buscar_usuario(usuarios, cpf)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Operação falhou! Usuário não encontrado.")

def buscar_usuario(usuarios, cpf):

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    
    return False

def listar_contas(contas):
    if len(contas) == 0:
        print("\nNão há contas cadastradas.")
        return

    for conta in contas:
        conta_string = f"""
        Agência: {conta['agencia']}
        Conta: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """

        print("========================")
        print(conta_string)

def main():
    # Quantidade máxima de operações de saque diárias
    MAX_DIARIO_SAQUE = 3
    # Valor máximo de saque por operação
    MAX_VALOR_SAQUE = 500
    # Agencia padrão das contas
    AGENCIA = "0001"

    saldo = 0
    saques_realizados = 0
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("\nInforme o valor de depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("\nInforme o valor do saque: "))

            saldo, extrato, saques_realizados = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                saques_realizados = saques_realizados,
                MAX_DIARIO_SAQUE = MAX_DIARIO_SAQUE,
                MAX_VALOR_SAQUE = MAX_VALOR_SAQUE
            )
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)
        
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            contas.append(conta) if conta else ()
        
        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)
        
        elif opcao == "7":
            break
        
        else:
            print("\nOperação falhou! Opção informada não existe, tente novamente.")

main()