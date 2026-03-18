### TIPOS DE DADOS ###
# CHAR = "S"
# VARCHAR = "Michael Saraiva Toniolo"
# INT = 123
# FLOAT/DOUBLE/DECIMAL = 1.33
# BOOLEAN/BOOL = FALSO OU VERDADEIRO (True/False)

## FAZENDO UM CADASTRO BÁSICO ##
nome = "Michael Saraiva Toniolo" #VARCHAR
idade = 34 #INT
altura = 1.81 #FLOAT/DOUBLE/DECIMAL

## CONCATENAÇÃO ##
print("Olá ", nome, ", sua idade é ", idade, " e sua altura é ", altura)
print(f"Olá {nome} sua idade é {idade} e sua altura é {altura}")
print("Olá {} sua idade é {} sua altura é {}".format(nome,idade,altura))

