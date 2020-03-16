#Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
#formadas pelos seus dois primeiros e dois últimos dígitos.
#Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.

def main():
    print("NÚMERO QUADRADO PERFEITO\n")
    
    numero = int(input("Digite um número: "))
    
    resultado = quadrado_perfeito(numero)
    
    print(f'O número {numero} {resultado} quadrado perfeito.')
    

def quadrado_perfeito(numero):
    
    raiz = numero ** (1/2)
    resto = raiz % 1
    
    if resto != 0:
        return "não é"
    else:
        return "é"
    

main()
    