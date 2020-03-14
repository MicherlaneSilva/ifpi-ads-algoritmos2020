from math import sqrt
print(" "*20, "DISTÂNCIA ENTRE DOIS PONTOS")

x1 = int(input("\nDigite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))

x2 = int(input("\nDigite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("\nA distância entre esses dois pontos é %.2f."%d)
