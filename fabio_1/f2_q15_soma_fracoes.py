#Leia 2 (duas) frações (numerador e denominador), 
# calcule e escreva a soma destas frações, e
# escrevendo o resultado em forma de fração.
print("++++++++ SOMA DE FRAÇÕES +++++++++++++")
numer1 = int(input("\nDigite o 1º numerador: "))
den1 = int(input("Digite o 1º denominador: "))
print("%d/%d"%(numer1, den1))

numer2 = int(input("\nDigite o 2º numerador: "))
den2 = int(input("Digite o 2º denominador: "))
print("%d/%d"%(numer2, den2))

soma_numeradores = numer1 * den2 + numer2 * den1
soma_denominadores = den2 * den1

print("%d/%d + %d/%d = %d/%d"%(numer1, den1, numer2, den2, soma_numeradores, soma_denominadores))