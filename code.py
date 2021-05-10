#tres tipos de triangulos#

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

def triangulo(n1, n2, n3):
  if (n1 == n2) and (n2 == n3):
    print('seu triangulo é equilátero')
  elif (n1 == n2) and (n1 != n2 or n1 != n3):
    print('seu triangulo é isósceles')
  else: 
    print('seu triangulo é escaleno')
      
triangulo(n1, n2, n3)
