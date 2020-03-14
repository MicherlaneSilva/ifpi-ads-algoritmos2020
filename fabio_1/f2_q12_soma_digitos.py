#Leia um número inteiro (4 dígitos),
#  calcule e escreva a soma dos 
# elementos que o compõem. Ex.:
#número = 9534 ; soma = 9+5+3+4 = 21.
print(" "*15, "SOMA DOS ALGARISMOS")
numero = int(input("Digite o número(4 dígitos): "))

um = numero // 1000
resto = numero % 1000
c = resto // 100
resto1 = numero % 100
d = resto1 // 10
u = resto1 % 10

soma_digitos = um + c + d + u
print("Número: %d \nSoma dos dígitos: %d + %d + %d + %d = %d"%(numero, um, c, d, u, soma_digitos))