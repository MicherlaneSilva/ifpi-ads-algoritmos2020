#Leia um número inteiro de minutos,
#  calcule e escreva quantos dias,
#  quantas horas e quantos minutos ele
#corresponde.

print(" "*15,"MINUTOS EM DIAS")

minuto = int(input("Digite a quantidade de minutos: "))

dias = minuto // 1440
resto = minuto % 1440
horas =  resto // 24
minutos = resto % 24

print("%d minutos são %d dia(s), %d hora(s) e %d minuto(s)."%(minuto, dias, horas, minutos))