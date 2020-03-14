#Leia um número inteiro de meses, 
#calcule e escreva quantos anos
#e quantos meses ele corresponde.

print(" "*15,"MESES EM ANOS")
mes = int(input("Digite a quantidade de meses: "))

anos = mes // 24
meses = mes % 24

print("{} meses são {} ano(s) e {} mes(es).".format(mes, anos, meses))