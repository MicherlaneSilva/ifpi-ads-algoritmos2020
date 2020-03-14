# Leia 1 (um) número de 2 (dois) dígitos,
# verifique e escreva se o algarismo da dezena é igual ou diferente
# do algarismo da unidade.

def main():

  print('************ DEZENAS E UNIDADES *************\n')
  numero = int(input("Digite um número inteiro: "))

  resultado = dezena_eh_igual_unidade(numero)

  print("\n"+"*"*45)
  print(f'A dezena do número {numero} é igual a unidade? {resultado}.')


def dezena_eh_igual_unidade(numero):

  dezena = numero // 10
  unidade = numero % 10

  if dezena == unidade:
    return "Sim"
  else:
    return "Não"

main()

