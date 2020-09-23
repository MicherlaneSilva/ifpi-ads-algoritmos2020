numeros = range(48, 58)
lower_case = range(97, 123)
upper_case = range(65, 91)
special_cases = "!@#$%^&*()-+"


def temNoConjunto(s, conjunto):
    
    for i in conjunto:
        if chr(i) in s:
            return True
        

def temSpecialCases(s):
    
    for crtere in special_cases:
        if crtere in s:
            return True
            
        
    
def minimoChr(s, n):
    
    qtdCaracteres = 0

    if temNoConjunto(s, numeros) == None:
        qtdCaracteres += 1
        
    if temNoConjunto(s, lower_case) == None:
        qtdCaracteres += 1
    
    if temNoConjunto(s, upper_case) == None:
        qtdCaracteres += 1

    if temSpecialCases(s) == None:
        qtdCaracteres += 1
    
    if n < 6:
        qtdCaracteres += (6 - n - qtdCaracteres)
    return qtdCaracteres


def main():
    
    n = int(input('Quantidade de caracteres: '))
    s = input('Senha: ')
    
    while n != len(s):
        print("Por favor digite a mesma quantidade de caracteres da senha.")
        n = int(input('Quantidade de caracteres: '))
        s = input('Senha: ')
        
        
    print(f'Você precisa de {minimoChr(s, n)} caracteres para gerar um senha forte.')
    

main()