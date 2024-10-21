#COMO EU FIZ:

#criando lista de numeros inteiros
listaBase = [1, 2, 3, 4, 5]

#criando lista vazia
listaFinal = []

for numeros in listaBase:
    transformação = float(numeros) #transformando esses numeros em float
    listaFinal.append(transformação) #adicionando a lista
    
print(listaFinal)



#maneira simplificada:


#criando lista de numeros inteiros
listaBase = [1, 2, 3, 4, 5]

#criando lista vazia
listaFinal = []

for numeros in listaBase:
    # transformando em float  e adicionando a lista
    listaFinal.append(float(numeros))
    
print(listaFinal)



