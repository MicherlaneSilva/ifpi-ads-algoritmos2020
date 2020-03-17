def main():
    
    nota = float(input('Digite a nota: '))
    conceito = atrib_conceito(nota)
    resultado = ver_aprovacacao(conceito)
    
    print(f'Conceito: {conceito}\nResultado: {resultado}')

def atrib_conceito(nota):
    
    if nota<= 4:
        return 'E'
    elif nota <= 6:
        return 'D'
    elif nota <= 7.5:
        return 'C'
    elif nota <= 9:
        return 'B'
    else:
        return 'A'

def ver_aprovacacao(conceito):
    
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        return 'Aprovado'
    else:
        return 'Reprovado'

main()
    
