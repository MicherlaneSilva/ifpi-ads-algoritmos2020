#Leia um número inteiro de metros,
# calcule e escreva quantos Km e quantos metros ele corresponde.

print("-=-=-=-=-=-=-= CONVERSOR DE METROS PARA QUILÔMETROS -=-=-=-=--==-")
metro = float(input("Digite o valor em metros: "))

quilometros = metro // 1000
metros = metro % 1000

print(f"{metro} metros são {quilometros}km e {metros} m.")