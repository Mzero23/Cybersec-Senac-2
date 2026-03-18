while (True):
    print("1- ADIÇÃO")
    print("2- SUB")
    print("3- MULT")
    print("4- DIVISÃO")
    print("0- SAIR")
    opcao = int(input("DIGITE UMA OPERAÇÃO MATEMÁTICA: "))
    
    if opcao == 0:
        print("VOCÊ ESCOLHEU SAIR!")
        break
    elif opcao == 1:
        print("ADIÇÃO SELECIONADA")
        num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
        num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
        print(f"A soma de {num1} + {num2} é: ", num1 + num2)
    elif opcao == 2:
        print("SUB SELECIONADA")
        num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
        num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
        print(f"A sub de {num1} - {num2} é: ", num1 - num2)
    elif opcao == 3:
        print("MUTL SELECIONADA")
        num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
        num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
        print(f"A sub de {num1} x {num2} é: ", num1 * num2)
    



