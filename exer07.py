cont1 = 0
cont2 = 0
for i in range(1, 10, 1):
    numero = int(input("digite um numero:"))
    if numero >= 10 and numero <= 20:
        cont1 = cont1 + 1
    else:
        cont2 = cont2 + 1
print(f"dentro do intervalo {cont1} fora do intervalo {cont2}")
