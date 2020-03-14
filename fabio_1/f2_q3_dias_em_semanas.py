#Leia um número inteiro de dias,
#calcule e escreva quantas semanas e quantos dias ele corresponde.
print("=.=.=.=.=.=.=.=. CONVERSOR SEMANAS .=.=.=.=.=.=.=")
dia = int(input("Digite a quantidade de dias: "))

semanas = dia // 7
dias = dia % 7

print("{} dias são {} semanas e {} dias.".format(dia,semanas,dias))