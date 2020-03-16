#Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
#nascimento e a data (dia, mês e ano) atual.

def main():
  print("IDADE\n")
  leitor = input('Data de hoje(dd/mm/aaaa): ').split('/')
  dia_h, mes_h, ano_h = int(leitor[0]), int(leitor[1]), int(leitor[2])

  leitor = input('\nData de nascimento(dd/mm/aaaa): ').split('/')
  dia_a, mes_a, ano_a  = int(leitor[0]), int(leitor[1]), int(leitor[2])

  ano, meses, dias = calcular_idade(dia_h, mes_h, ano_h, dia_a, mes_a, ano_a)

  print(f"\nSua idade é {ano} anos, {meses} meses e {dias} dias.")

def calcular_idade(dia_h, mes_h, ano_h, dia_a, mes_a, ano_a):

   total_dias_hoje = ano_h * 365 + mes_h * 30 + dia_h
   total_dias_aniversario = ano_a * 365 + mes_a * 30 + dia_a
   dias_vividos = (total_dias_hoje - total_dias_aniversario)
   
   if total_dias_aniversario < total_dias_hoje:    
        anos = dias_vividos //365
        resto = dias_vividos % 365
        meses = resto // 30
        dias = resto % 30  
   else:
       anos = 0
       meses = 0
       dias = 0   

   return anos, meses, dias

  
main()