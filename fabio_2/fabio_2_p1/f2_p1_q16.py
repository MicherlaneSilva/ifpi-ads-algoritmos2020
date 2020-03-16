#Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
#ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
#final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
#escreva “Reprovado”.
#Escreva um algoritmo para ler um número e verificar se ele obedece a esta característica.


def main():
    
    resultado = ''
    print("\nRESULTADO AVALIAÇÃO\n")
    
    nota1 = float(input('1º Nota: '))
    nota2 = float(input('2º Nota: '))
    
    resultado, media = verificar_aprovacao(nota1, nota2, resultado)
    
    if resultado == "Reprovado":
        nota_exame = float(input("\nNota do exame: "))
        resultado, media = verificar_aprovacao(nota_exame, media, resultado)
    
    print(f"\nRESULTADO: {resultado}\nMédia final: {media}")


def media(nota1, nota2):
    return (nota1 + nota2)/2

def verificar_aprovacao(nota1, nota2, resultado):
    
    if resultado == '':
        if media(nota1, nota2)<7:
            return "Reprovado", media(nota1, nota2)
        else:
            return "Aprovado", media(nota1, nota2)
    else:
        if media(nota1, nota2)<5:
            return "Reprovado", media(nota1, nota2)
        else:
            return "Aprovado", media(nota1, nota2)

main()