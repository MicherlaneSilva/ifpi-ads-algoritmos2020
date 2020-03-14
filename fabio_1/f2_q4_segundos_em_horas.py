#Leia um número inteiro de segundos, calcule e escreva quantas horas, 
# quantos minutos e quantos
#segundos ele corresponde.

print(" "*2015,"CONVERSOR DE SEGUNDOS"," "*20)

segundo = int(input("Digite a quantidade de segundos: "))

horas = segundo // 3600
resto = segundo % 3600
minutos = resto // 60
segundos = resto % 60

print("{} segundos são {} horas, {} minutos e {} segundos.".format(segundo, horas, minutos, segundos))