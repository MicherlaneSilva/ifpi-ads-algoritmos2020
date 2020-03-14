#  Um algoritmo para gerenciar os saques de um caixa eletrônico
#  deve possuir algum mecanismo para decidir o numero de notas
#  de cada valor que deve ser disponibilizado para o cliente que
#  realizou o saque. Um possível critério seria o da "distribuição ótima"
#  no sentido de que as notas de menor valor disponíveis fossem
#  distribuídas em número mínimo possível. Por exemplo,
#  se a maquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1,
#  para uma quantia solicitada de R$ 87, o algoritmo deveria indicar uma
#  nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1.
#  Escreva um algoritmo que receba o valor da quantia solicitada e retorne
#  a distribuição das notas de acordo com o critério da distribuição ótima.

print("=-"*10, "CAIXA ELETRÔNICO","-="*10,"\n")

valor = int(input("Digite o valor de saque: "))

notas100 = valor // 100
resto1 = valor % 100
notas50 = resto1 // 50
resto2 = resto1 % 50
notas20 = resto2 // 20
resto3 = resto2 % 20
notas10 = resto3 // 10
resto4 = resto3 % 10
notas5 = resto4 // 5
notas1 = resto4 % 5

print("\nOPERAÇÃO REALIZADA COM SUCESSO!\n")
print("%d notas de R$ 100,00"%notas100)
print("%d notas de R$ 50,00"%notas50)
print("%d notas de R$ 20,00"%notas20)
print("%d notas de R$ 10,00"%notas10)
print("%d notas de R$ 5,00"%notas5)
print("%d notas de R$ 1,00"%notas1)