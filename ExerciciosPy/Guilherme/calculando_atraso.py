def atrasou(atrasoEmDias):
 
 if atrasoEmDias > 0:
     if atrasoEmDias <= 3:
         return 0.50
     elif atrasoEmDias <= 7:
         return 1.00
     else:
         return 2
     
def calculo(atrasoEmDias, atrasou):
    
    multa = atrasoEmDias * atrasou
    return multa
    

atrasoEmDias = float(input("Digite o numero de atraso em dias:")) 


print(f"O valor da sua multa é R${calculo(atrasoEmDias, atrasou(atrasoEmDias))}")