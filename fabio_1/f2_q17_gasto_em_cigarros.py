#Calcule a quantidade de dinheiro gasta por um fumante.
#Dados de entrada: o número de anos que ele fuma,
#o no de cigarros fumados por dia e o preço de
#uma carteira (1 carteira tem 20 cigarros).

print("    Saiba quanto você gasta com cigarros")

anos = int(input("Há quantos anos você fuma? "))
cigarros = int(input("Você fuma quantos cigarros por dia? "))
preco = float(input("Digite o preço da carteira de cigarro: "))

valor_cigarro = preco / 20 
gasto = anos * 365 * cigarros * valor_cigarro


print("Em todos esses anos você gastou R$ %.2f em cigarros."%gasto)