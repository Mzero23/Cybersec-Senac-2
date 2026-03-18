### NOSSA CALCULADORA ###

print("BEM VINDO!")
nome = input("DIGITE SEU NOME: ")

print(f"{nome}, selecione um número para escolher a operação")
opcao = int(input("1- ADIÇÃO\n2-SUBTRAÇÃO\n3-MULTIPLICAÇÃO\n4-DIVISÃO\n0-SAIR| "))

# == IGUAL
# != DIFERENTE
# > MAIOR QUE
# < MENOR QUE
# >= MAIOR IGUAL
# <= MENOR IGUAL
# === IDÊNTICO (MESMO TIPO DE DADO) ***

### AGORA O ROLÊ VALIDANDO
if opcao == 1:
    num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
    num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
    print(f"O RESULTADO DA SOMA ENTRE {num1} + {num2} é: ", num1 + num2)

elif opcao == 2:
    num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
    num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
    print(f"O RESULTADO DA SUB ENTRE {num1} - {num2} é: ", num1 - num2)

elif opcao == 3:
    num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
    num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
    print(f"O RESULTADO DA MULTI ENTRE {num1} x {num2} é: ", num1 * num2)

elif opcao == 4:
    num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
    num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
    print(f"O RESULTADO DA DIVISÃO ENTRE {num1} / {num2} é: ", num1 // num2)
else:
    print("SAINDO DA APLICAÇÃO")
    