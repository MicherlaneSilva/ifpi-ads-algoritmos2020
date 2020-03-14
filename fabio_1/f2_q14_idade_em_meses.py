#Leia a idade de uma pessoa expressa em dias e
#escreva-a expressa em anos, meses e dias.
print(" "*20,"Saiba quantos anos você tem")
dia1 = int(input("Digite quantos dias você viveu: "))

anos = dia1 // 365
resto = dia1 % 365
meses = resto // 30
dias = resto % 30

print("Você tem {} anos, {} meses e {} dias.".format(anos, meses, dias))