saldo = 1000  # Saldo inicial

while True:
    print("\n--- Menu do Caixa Eletrônico ---")
    print("1. Ver Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")
    
    opcao = input("Digite sua opção: ")
    
    if opcao == '1':
        print(f"Saldo Atual: R${saldo:.2f}")
    elif opcao == '2':
        try:
            valor = float(input("Digite o valor a depositar: "))
            if valor > 0:
                saldo += valor
                print(f"R${valor:.2f} depositado com sucesso. Novo Saldo: R${saldo:.2f}")
            else:
                print("O valor do depósito deve ser positivo.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    elif opcao == '3':
        try:
            valor = float(input("Digite o valor a sacar: "))
            if valor > 0:
                if valor <= saldo:
                    saldo -= valor
                    print(f"R${valor:.2f} sacado com sucesso. Novo Saldo: R${saldo:.2f}")
                else:
                    print("Saldo insuficiente.")
            else:
                print("O valor do saque deve ser positivo.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    elif opcao == '4':
        print("Obrigado por usar o Caixa Eletrônico. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
