nome = input("DIGITE SEU NOME: ")
sobrenome = input("DIGITE SEU SOBRENOME: ")

idade = int(input("DIGITE SUA IDADE: "))
dia = input("DIGITE O DIA DE SEU NASCIMENTO: ")
mes = input("DIGITE O MÊS DE NASCIMENTO: ")
genero = input("DIGITE O GENERO(m/f): ")

#VALIDAÇÕES
if idade >= 18 and genero == "m":
    print("É OBRIGATÓRIO O ALISTAMENTO MILITAR: ")
elif idade >= 18 and genero == "f":
    print("ATENDE EM MAIORIDADE PORÉM NÃO É OBRIGADO MULHERES NO ALISTAMENTO!")
else:
    print("NÃO É NECESSÁRIO ALISTAMENTO MILITAR!")
