def main():
	
	linha_completa()
	do_twice(coluna_twice)
	linha_completa()
	do_twice(coluna_twice)
	linha_completa()

def linha():
	print('+',' -' * 4, end= " ")

def fim_linha():
	print("+")

def coluna():
	print("|","  "*4, end=" ")

def fim_coluna():
	print("|")

def do_twice(f):
	f()
	f()

def do_four(f):
	do_twice(f)
	do_twice(f)

def coluna_twice():
	do_twice(coluna)
	fim_coluna()
	do_twice(coluna)
	fim_coluna()

def linha_completa():
	do_twice(linha)
	fim_linha()


main()