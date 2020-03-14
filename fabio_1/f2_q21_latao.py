#Sabendo que latão é constituído de 70% de cobre e 30% de zinco, 
#escreva um algoritmo que calcule a quantidade de cada um desses 
#componentes para se obter certa quantidade de latão (em kg), informada pelo usuário.

print(""*20, "CÁLCULO DOS COMPONENTES DE LATÃO")

quant_latao = float(input("\nDigite quantos quilogramas de latão você quer produzir: "))

cobre = 0.70 * quant_latao
zinco = 0.30 * quant_latao

print("São necessários %.2f kg de zinco e %.2f kg de cobre."%(zinco,cobre))