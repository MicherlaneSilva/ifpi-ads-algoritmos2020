#Leia um número inteiro (4 dígitos binários), 
#calcule e escreva o equivalente na base decimal.

print(" "*15,"BASE BINÁRIA PARA DECIMAL")
numero = int(input("Digite o número de 4 dígitos em base binária: "))

alg1 = numero // 1000
resto = numero % 1000
alg2 = resto // 100
resto2 = resto % 100
alg3 = resto2 // 10
alg4 = resto2 % 10
b_decimal = (alg4 * 2 ** 0) + alg3 * 2 ** 1 + alg2 * 2 ** 2 + alg1 * 2 ** 3

print("%d equivale %d em base 10."%(numero, b_decimal))
