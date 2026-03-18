while (True):
    print("1- ADIÇÃO")
    print("2- SUB")
    print("3- MULT")
    print("4- DIVISÃO")
    print("0- SAIR")
    opcao = int(input("DIGITE UMA OPÇÃO: "))

    match opcao:
        case 1:
            print("ADIÇÃO SELECIONADA")
            num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
            num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
            print(f"A soma de {num1} + {num2} é: ", num1 + num2)
        case 2:
            print("ADIÇÃO SELECIONADA")
            num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
            num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
            print(f"A soma de {num1} + {num2} é: ", num1 + num2)
        case 3:
            print("ADIÇÃO SELECIONADA")
            num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
            num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
            print(f"A soma de {num1} + {num2} é: ", num1 + num2)
        case _:
            print("SAINDO DA APLICAÇÃO")
            break

