# Leia um número (vetor com 8 elementos) na base binária, 
# calcule e escreva este número na base
# hexadecimal e na base decimal.

letra_hexadecimal = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}


def converter_em_inteiros(numero_binario):
    for i in range(len(numero_binario)):
        numero_binario[i] = int(numero_binario[i])
        
        
def mudar_ordem(numero_binario):
    
    numero_reordernado = []
    for i in range(len(numero_binario) -1,  -1, -1):
        numero_reordernado.append(numero_binario[i])
    
    return numero_reordernado


def converter_base(numero_binario, base):
    Nbase = 0
    for i in range(len(numero_binario)):
        Nbase += (numero_binario[i] * base ** i)   
    return Nbase
     
        
def converter_decimal(numero_binario):
    
    numero_binario = mudar_ordem(numero_binario)
    Ndecimal = converter_base(numero_binario, 2)
    return Ndecimal


def valor_hexa(valor_decimal):
    if valor_decimal not in letra_hexadecimal:
        return valor_decimal
    else:
        return letra_hexadecimal[valor_decimal]
    

def converter_hexadecimal(numero_binario):
    Nhexadecimal = ""
    if  len(numero_binario) % 4 != 0:
        numero_binario = [0] * (4 - (len(numero_binario)% 4)) + numero_binario
        
    for i in range(len(numero_binario) // 4): 
          Nhexadecimal += str(valor_hexa(converter_decimal(numero_binario[(4 * i): (4 * i) + 4])))
    
    return Nhexadecimal

   
def main():
    print("** CONVERSÃO DE BASE ***")
    
    numero_binario = list(input("Digite o número em binário: "))
    converter_em_inteiros(numero_binario)
        
    print(f'Número no sistema decimal: {converter_decimal(numero_binario)}')
    print(f'Número em hexadecimal: {converter_hexadecimal(numero_binario)}')
    
main()