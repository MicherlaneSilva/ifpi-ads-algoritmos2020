#Leia um número inteiro (3 dígitos), 
# calcule e escreva a soma do número com seu inverso.
#(Ex.: número = 532 ; inverso = 235 ; 
# soma = 532 + 235 = 767).

print(" "*15, "SOMA ENTRE UM NÚMERO E SEU INVERSO")
numero = int(input("Digite o número(3 dígitos): "))

c = numero // 100
resto = numero % 100
d = resto // 10
u = resto % 10

inverso = u * 100 + d * 10 + c
soma = numero + inverso

print("%d + %d = %d"%(numero, inverso, soma))