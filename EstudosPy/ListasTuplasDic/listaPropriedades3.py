import random #importando biblioteca random e susas funcionalidades

#criando lista
cidades = ['Maceió','Recife','Pernambuco','Ceará']

#sorteando indices numa lista usando random.choice
escolhida = random.choice(cidades)

#printando resultado
print(f'a cidade escolhida é {escolhida}')

#maneira simplificada

#sorteando indices numa lista usando random.choice e printando resultado
print(f'a cidade escolhida é {random.choice(cidades)}')

