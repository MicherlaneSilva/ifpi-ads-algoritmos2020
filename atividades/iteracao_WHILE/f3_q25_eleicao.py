# Em uma eleição presidencial existem 3 (três) candidatos. Os votos são informados através de códigos.
# Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:

# Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva:
# a) total de votos para cada candidato;
# b) total de votos nulos;
# c) total de votos em branco;
# d) quem venceu a eleição.

def quem_venceu(candidato_a, candidato_b, candidato_c):
    
    if candidato_a > candidato_b and candidato_a > candidato_c:
        return "Candidato A"
    elif candidato_b > candidato_a and candidato_b > candidato_c:
        return "Candidato B"
    elif candidato_c > candidato_a and candidato_c > candidato_b:
        return "Candidato C"
    else:
        return "Empate técnico"
    
def main():
    
    candidato_a = 0
    candidato_b = 0
    candidato_c = 0
    nulo = 0
    branco = 0
    contador = 0
    
    n = int(input("Digite a quantidade de eleitores: "))
    
    print("""REGRAS
· 1, 2, 3 = voto para os respectivos candidatos;
· 9 = voto nulo;
· 0 = voto em branco.""")
    
    while contador < n:
        print(f"\nEleitor {contador + 1}")
        voto = int(input("Voto: "))
        
        if voto == 1:
            candidato_a += 1
        elif voto == 2:
            candidato_b += 1
        elif voto == 3:
            candidato_c += 1
        elif voto == 9:
            nulo += 1
        elif voto == 0:
            branco += 1
        
        contador += 1
    
    print(f""" RESULTADOS
Total de votos para o candidato A: {candidato_a}
Total de votos para o candidato B: {candidato_b}
Total de votos para o candidato C: {candidato_c}
Total de votos nulos: {nulo}
Total de votos em branco: {branco};
Vencedor da Eleição: {quem_venceu(candidato_a, candidato_b, candidato_c)}""")


main()