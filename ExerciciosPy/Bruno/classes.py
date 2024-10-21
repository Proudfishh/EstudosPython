class Convidado:
    def __init__(self, nome, idade, permissao):
        self.nome = nome
        self.idade = idade
        self.permissao = permissao.upper()

    def tem_idade_suficiente(self, idade_minima):
        return self.idade >= idade_minima

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Permissão: {self.permissao}"

convidado1 = Convidado('gabriel', 20, 'sim')
convidado2 = Convidado('bruno', 17, 'sim')
convidado3 = Convidado('lucas', 17, 'nao')

idade_minima = 18

print(convidado1.tem_idade_suficiente(idade_minima))
print(convidado2.tem_idade_suficiente(idade_minima))
print(convidado3.tem_idade_suficiente(idade_minima))

print(convidado1)
print(convidado2)
print(convidado3)