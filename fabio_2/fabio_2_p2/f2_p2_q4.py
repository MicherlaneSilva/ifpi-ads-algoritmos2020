#Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
#o "Aprovado", se a média alcançada for maior ou igual a sete;
# "Reprovado", se a média for menor do que sete;
# "Aprovado com Distinção", se a média for igual a dez.

def main():
    
    print("BOLETIM")
    nota1 = float(input("1ª nota: "))
    nota2 = int(input('2ª nota: '))
    
    media, resultado = verificar_aprovacao(nota1, nota2)
    
    print("\nMédia: %.2f\nResultado: %s"%(media, resultado))

def  verificar_aprovacao(nota1, nota2):
    
    media = (nota1 + nota2)/2
    
    if media < 7:
        return media, 'Reprovado'
    elif media == 10:
        return media, 'Aprovado com Distinção'
    else:
        return media, 'Aprovado'


main()