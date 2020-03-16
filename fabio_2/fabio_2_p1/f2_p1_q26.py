#Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.

def main():

  print('TRIÂNGULO RETÂNGULO')
  l1 = int(input("1º lado: "))
  l2 = int(input("2º lado: "))
  l3 = int(input("3º lado: "))

  triangulo, hipotenusa, cateto1, cateto2 = id_partes_triangulo(l1, l2, l3)

  print(f'\n{triangulo}\nHipotenusa: {hipotenusa}\nCateto 1: {cateto1}\nCateto 2: {cateto2}')

def maior_lado(l1,l2,l3):
  if l1 > l2 and l1>l3:
    return l1, l2, l3
  elif l2> l1 and l2>l3:
    return l2, l1, l3
  else:
    return l3, l1, l2


def verificar_triangulo(l1, l2, l3):
  maior, menor1, menor2 = maior_lado(l1, l2, l3)

  if maior < menor1+menor2:
    return "existe"
  else:
    return "não existe"


def id_partes_triangulo(l1, l2, l3):
  
  if verificar_triangulo(l1, l2, l3) == 'existe':
    if l1** 2 == l2 ** 2 + l3 **2:
      return 'Triângulo retângulo',l1, l2, l3
    elif l2 **2 == l1 ** 2 + l3**2:
      return  'Triângulo retângulo',l2, l1, l3
    elif l3 ** 2 == l1**2 +l2**2:
      return  'Triângulo retângulo',l3, l1, l2
    else:
      return '\aO triângulo não é retângulo','inválida', 'inválido', 'inválido'
  else:
    return '\aTriângulo inexistente','inválida', 'inválido', 'inválido'

main()