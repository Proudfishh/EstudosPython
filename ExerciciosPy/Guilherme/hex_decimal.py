
tipo = int(input("Digite 1 para numero de registro 2 para hexadecimal"))
numero = input("Qual o numero quer converter ")

if tipo == 1:
    numRes = int(numero,16)
    print(f"Seu numero de registro é: {numRes}")
elif tipo == 2:
    numHex = hex(int(numero))
    print(f"Seu numero em hexadecimal é: {numHex}")
    