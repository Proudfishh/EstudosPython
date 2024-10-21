def verificandoSeETriangulo(lado1, lado2, lado3):
 if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
  return True
     
def verificarTriEquilatero(lado1, lado2, lado3):
 if lado1 == lado2 == lado3:
  return True

def verificarTriIsoceles(lado1, lado2, lado3):
 if lado1 == lado2:
  return True
 if lado2 == lado3:
  return True
 if lado1 == lado3:
  return True
 

lado1 = float(input("Digite o primeiro lado:"))
lado2 = float(input("Digite o segundo lado:"))
lado3 = float(input("Digite o terceiro lado:"))

checktriangulo = verificandoSeETriangulo(lado1, lado2, lado3)
equilatero = verificarTriEquilatero(lado1, lado2, lado3)
isoceles = verificarTriIsoceles(lado1, lado2, lado3)

if checktriangulo == True:
 if equilatero == True:
  print("é equilatero")
 elif isoceles == True:
  print("é isoceles")
 else:
  print("é escaleno")

else:
 print("não é triangulo")
 


