#Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
#(três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
#formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
#escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).

def main():

  print("************** CLASSIFICAÇÃO DE TRIÂNGULO ***************\n")

  l1 = int(input('>> 1º lado: '))
  l2 = int(input('>> 2º lado: '))
  l3 = int(input('>> 3º lado: '))

  resultado = classificacao_triangulo(l1, l2, l3)
  
  print("\n",resultado)


def maior_lado(l1, l2, l3):

  if l1 > l2 and l1 > l3:
    return l1, l2, l3
  elif l2 > l1 and l2 > l3:
    return l2, l1, l3
  else:
    return l3, l1, l2


def classificacao_triangulo(l1, l2, l3):

  maior, menor1, menor2 = maior_lado(l1, l2, l3)

  if maior >= menor1 + menor2:
    return "Os comprimentos dos lados enviados não formam um triângulo."
  elif l1 == l2 == l3:
    return "Triângulo equilátero."
  elif l1 != l2 != l3:
    return "Triângulo escaleno."
  else:
    return "Triângulo isósceles."


main()