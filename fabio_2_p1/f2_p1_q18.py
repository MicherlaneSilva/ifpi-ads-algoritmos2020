#Leia dois valores e uma das seguintes operações a 
# serem executadas (codificadas da seguinte forma: 1 –
#Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão).
#  Calcule e escreva o resultado dessa operação
#sobre os dois valores lidos.

def main():
    
    print("CALCULADORA\n")
    
    num1 = int(input('Número: '))
    operador = input('Operador(+ , -, *, /): ')
    num2 = int(input('Número: '))
    
    resultado = calculadora(num1, operador, num2)
    
    print("\nResultado: ",resultado)


def calculadora(num1, operador, num2):
    
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 != 0:
            return num1/num2
        else:
            return "Impossível divisão por zero."
    else:
        return "Operador inválido"


main()
