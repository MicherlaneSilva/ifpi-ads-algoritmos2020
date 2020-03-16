#Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
#um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
#não pode ser negativo.

def main():
    
    print('Área do retângulo\n')
    
    print("Coordenada 1º ponto")
    x1 = float(input("x1: "))
    y1 = float(input('y1: '))
    
    print("\nCoordenada 1º ponto")
    x2 = float(input("x2: "))
    y2 = float(input('y2: '))
    
    area = calc_area(x1, y1, x2, y2)
    
    print("Área do retângulo: {:.2}".format(area))


def calc_area(x1, y1, x2, y2):
    
    area = (x2 - x1) * (y2 - y1)
    
    if area < 0:
        area = ((-1) * area)
    
    return area

main()