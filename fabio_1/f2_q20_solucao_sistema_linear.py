print(" "*20, "SOLUÇÃO DO SISTEMA LINEAR")
print("\n")

a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))
d = float(input("Digite o coeficiente 'd': "))
e = float(input("Digite o coeficiente 'e': "))
f = float(input("Digite o coeficiente 'f': "))

print("\n%.2fx + %.2fy = %.2f\n%.2fx + %.2fy = %.2f"%(a, b, c, d, e, f))

x = (c * e - b * f) / (a * e - b * d)
y = (a * f - c * d) / (a * e - b * d)

print("S = {(%.2f, %.2f)}"%(x, y))