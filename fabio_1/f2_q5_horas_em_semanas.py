#Leia um número inteiro de horas, 
# calcule e escreva quantas semanas, 
# quantos dias e quantas horas ele
#corresponde.
print(" "*15,"CONVERSOR DE HORAS")
hora = int(input("Digite a quantidade de horas: "))

semanas = hora // 168
resto = hora % 168
dias =  resto // 24
horas = resto % 24

print("{} horas são {} semana(s), {} dia(s) e {} hora(s).".format(hora, semanas, dias, horas))