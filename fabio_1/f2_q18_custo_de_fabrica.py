#O custo ao consumidor de um carro novo é
#a soma do custo de fábrica com a percentagem do
#distribuidor e dos impostos (aplicados ao custo de fábrica).
# Supondo que a percentagem do distribuidor seja de 28% 
# e os impostos de 45%, escreva um algoritmo que leia o
#  custo de fábrica de um carro e escreva o custo ao consumidor.

print("     CÁLCULO VALOR DE REVENDA")
print("\n")

per_distribuidor = 0.28
impostos = 0.45

custo_fabrica = float(input("Valor do custo de fábrica: "))

custo_consumidor = custo_fabrica + (custo_fabrica * impostos) + (custo_fabrica * per_distribuidor )

print("\nCusto final do carro: R$ %.2f"%custo_consumidor)