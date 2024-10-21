def semana(indice):
    if indice == 0:
        return "segunda-feira"
    if indice == 1:
        return "terça-feira"
    if indice == 2:
        return "quarta-feira"
    if indice == 3:
        return "quinta-feira"
    if indice == 4:
        return "sexta-feira"
    if indice == 5:
        return "sábado"
    if indice == 6:
        return "domingo"

numLivros = []

for x in range(7):
 numeroDeLivros = int(input("Quantos livros foram emprestados ao logo da semana: "))
 numLivros.append(numeroDeLivros)

print(f"O número total de livros emprestados foi {sum(numLivros)}")
print(f"A média diaria de empréstimos é {sum(numLivros)/7}")
print(f"O dia com o maior número de empréstimos foi {semana(numLivros.index(max(numLivros)))}")


    
    