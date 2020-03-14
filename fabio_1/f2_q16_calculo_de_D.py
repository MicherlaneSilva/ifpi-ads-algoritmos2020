print("============= CÁLCULO DE D ===============")

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
c = int(input("Digite mais um número inteiro: "))

r = (a + b) ** 2
s = (c + b) ** 2
d = (r + s) / 2

print("\nO valor de D é %.2f"%d)