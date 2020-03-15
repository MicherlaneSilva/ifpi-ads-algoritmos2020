#  Realize arredondamentos de números utilizando a
#  regra usual da matemática: se a parte fracionaria for
#  maior do que ou igual a 0,5, o numero é arredondado para
#  o inteiro imediatamente superior, caso
#  contrario, é arredondado para o inteiro imediatamente inferior.

def main():
    print(" "*50+'ARREDONDAMENTO\n')
    
    numero = float(input("Digite um número real: "))
    print("\nO número arredondado: ", arredondamento(numero))
    
 
def arredondamento(numero):
    
    parte_fracionaria = numero % 1
       
    if parte_fracionaria >= 0.5:        
        return numero + (1 - parte_fracionaria)
    else:
        return numero - parte_fracionaria

main()
    