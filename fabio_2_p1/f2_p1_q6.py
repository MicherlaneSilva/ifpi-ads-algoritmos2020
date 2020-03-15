#Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
#se os 3 (três) números formam um triângulo
# (a soma dos ângulos internos é igual a 180o). Se formam,
#verifique se formam um triângulo acutângulo (3 ângulos < 90o),
# retângulo (1 ângulo = 90o) ou
#obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).

def main():
  print("************* TRIÂNGULO ***************\n")

  angle1 = int(input(">> 1º ângulo: "))
  angle2 = int(input(">> 2º ângulo: "))
  angle3 = int(input(">> 3º ângulo: "))

  resultado = classificacao_triangulo(angle1, angle2, angle3)

  print("\n", resultado)

def classificacao_triangulo(angle1, angle2, angle3):
  
  soma_angulo = angle1 + angle2 + angle3
  if soma_angulo not in range(1,181) and angle1 != 0 and angle2 != 0  and angle3 != 0:
    return "O triângulo não existe."
  elif angle1 == 90 or angle2 == 90 or angle3 == 90:
    return "Triângulo retângulo."
  elif angle1 > 90 or angle2 > 90 or angle3 > 90:
    return "Triângulo obtusângulo."
  else:
    return "Triângulo acutângulo."
  

main()
