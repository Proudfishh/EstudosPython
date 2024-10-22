while True:
    try:
        peso = float(input("Digite seu peso em kg: "))
        
        if peso <= 0:
            raise ValueError("Peso deve ser um número positivo.")
        
        altura = float(input("Digite sua altura em metros: "))
        if altura <= 0:
            raise ValueError("Altura deve ser um número positivo.")
        
        break
    except ValueError as e:
        print(f"Erro: {e}")

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade Grau 1"
elif imc < 40:
    classificacao = "Obesidade Grau 2"
else:
    classificacao = "Obesidade Grau 3"

print(f"Classificação: {classificacao}")