#Leia 3 (três) números e escreva-os em ordem crescente.

def main():

  print("+++++++++++ ORDEM CRESCENTE +++++++++++++")

  n1 = int(input("Digite o 1º número: "))
  n2 = int(input('Digite o 2º número: '))
  n3 = int(input('Digite o 3º número: '))

  pri, seg, ter = ordem_crescente(n1, n2, n3)

  print(f'\nClassificação em ordem crescente: {pri} - {seg} - {ter}')


def ordem_crescente(n1, n2, n3):
  '''Recebe três números inteiros e coloca-os em ordem crescente.'''

  if n1 > n2 and n1 > n3:
    if n2 > n3:
      return n3, n2, n1
    else:
      return n2, n3, n1
  
  elif n2> n1 and n2 > n3:
    if n1 > n3:
      return n3, n1, n2
    else:
      return n1, n3, n2

  else:
    if n1 > n2:
      return n2, n1, n3
    else:
      return n1, n2, n3


main()
