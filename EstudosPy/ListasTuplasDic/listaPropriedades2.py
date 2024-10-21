import random #importando biblioteca random e suas funcionalidades

#criando uma lista
cidades = ['Maceió','Recife','Pernambuco','Ceará']

#input de informação
adição = input('Escolha uma cidade: ')

#adicionando a lista informação
cidades.append(adição)

print(cidades)

#maneira simplificada:

cidades = ['Maceió','Recife','Pernambuco','Ceará']

adição = cidades.append(input('Escolha uma cidade: '))

print(cidades)
