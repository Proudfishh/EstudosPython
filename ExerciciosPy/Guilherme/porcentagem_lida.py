def porcentagem(numeroTotalLidas, numeroTotalPag):
    
    if numeroTotalLidas >= 0 and numeroTotalPag >= 0:
        
        return ((numeroTotalLidas / numeroTotalPag) * 100)

def lidas(numeroTotalLidas, numeroTotalPag):
 
 if numeroTotalLidas > numeroTotalPag:
  while True: 
   numeroTotalLidas = int(input("Digite um número correspondente ao total do livro: "))
   if numeroTotalLidas == numeroTotalPag:
     
     return numeroTotalLidas


numeroTotalPag = int(input("Digite o número total de páginas: "))

numeroTotalLidas = int(input("Digite o número total de páginas lidas: "))

if numeroTotalLidas > numeroTotalPag:
 numeroTotalLidas = lidas(numeroTotalLidas, numeroTotalPag)
    
print(f"voce leu {porcentagem(numeroTotalLidas, numeroTotalPag)}% do livro")



