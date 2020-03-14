#eia um número inteiro (3 dígitos), 
# calcule e escreva a diferença entre o número e seu inverso.
print(" "*15, "DIFERENÇA ENTRE UM NÚMERO E SEU INVERSO")
numero = int(input("Digite o número(3 dígitos): "))

c = numero // 100
resto = numero % 100
d = resto // 10
u = resto % 10

inverso = u * 100 + d * 10 + c
diferenca = numero - inverso

print("%d - %d = %d"%(numero, inverso, diferenca))