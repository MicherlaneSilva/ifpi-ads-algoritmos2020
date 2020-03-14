#Leia a idade de uma pessoa expressa em anos, 
#meses e dias e escreva-a expressa apenas em dias.
print(" "*20, "IDADE EM DIAS")
anos = int(input("Escreva quantos anos você tem: "))
meses = int(input("Agora escreva quantos meses você tem: "))
dias = int(input("E por fim, quantos dias: "))

dias2 = (anos * 365) + (meses * 30)  + dias

print("Você viveu %d dias."%dias2)