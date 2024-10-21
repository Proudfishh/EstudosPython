listaDeNumeros = []

for num in range(2):
 soma = int(input("digite o primeiro e segundo numero: "))
 listaDeNumeros.append(soma)


# criando função normal de soma
def funçãoSoma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

#chamando função normal
print(funçãoSoma(listaDeNumeros[0], listaDeNumeros[1]))

#criando função lambda, o termo lambda identifica a função anônima 
funçãoSomaLamb = lambda numero1, numero2 : numero1 + numero2

#chamando função lambda
print(funçãoSomaLamb(listaDeNumeros[0],listaDeNumeros[1]))