from math import sqrt

#Leia os coeficientes (A, B e C) de uma equações de 2° grau 
# e escreva suas raízes. Vale lembrar que o
#coeficiente A deve ser diferente de 0 (zero).

def main():
    print("EQUAÇÃO DO SEGUNDO GRAU\n")
    
    a = int(input("Valor do coeficiente A: "))
    b = int(input("Valor do coeficiente B: "))
    c = int(input("Valor do coeficiente C: "))
    
    print('%dx²+%dx+%d = 0'%(a,b,c))
    print('\n'+solucao(a,b,c))

def calcular_delta(a, b, c):
    
    return b ** 2 - 4 * a*  c

def solucao(a, b, c):
    if a != 0:
        delta = calcular_delta(a, b, c)
        if delta == 0:
            return "Duas raízes reais e iguais:\nr1 = r2 = %.2f"%(b/2 * a)
        elif delta > 0:
            r1 = (-b + sqrt(delta))/2* a
            r2 = (-b - sqrt(delta))/2* a
            return "Duas raízes reais diferentes:\n r1 = %.2f, r2 = %.2f"%(r1, r2)
        else:
            return "Não possui raízes reais."
    else:
        return "A equação digitada é do primeiro grau cuja solução é %.2f"%(-1*c/b)
        
    
main()