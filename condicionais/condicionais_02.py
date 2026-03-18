### CONDICIONAIS COM MAIS DE UM VALOR ###
nome = input("DIGITE SEU NOME: ")
n1 = float(input("DIGITE UMA PRIMEIRA NOTA "))
n2 = float(input("DIGITE A SEGUNDA NOTA: "))
frequente = input("DIGITE SE ALUNO FREQUENTE (s/n): ")
media = round(((n1 + n2) / 2), 2)

if  (media >= 7 and frequente == "s"): #or
    print(f"O ALUNO {nome} tem a nota 1 [{n1}] e nota 2 [{n2}] e então foi aprovado com média de: [{media}]")
elif (media >= 5 and frequente == "s"):
    print(f"O ALUNO {nome} tem a nota 1 [{n1}] e nota 2 [{n2}] precisa de recuperação com média de: [{media}]")
else:
    print(f"ALASTROU E REPROVOU!COM MÉDIA [{media}]")

