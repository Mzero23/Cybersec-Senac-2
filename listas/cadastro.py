pessoa1 = ["Robson", 25,"01/01/2000", "Observação" ]
pessoa2 = ["Bruno", 30, "01/01/2000", "Obs2"]

if pessoa1[1] > pessoa2[1]:
    print(f"{pessoa1[0]} é mais velho que {pessoa2[0]}")
elif pessoa1[1] == pessoa2[1]:
    print(f"A idade de {pessoa1[0]} é igual de {pessoa2[0]}")
else:
    print(f"{pessoa2[0]} é mais velho que {pessoa1[0]}")