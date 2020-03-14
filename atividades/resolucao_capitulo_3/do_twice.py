def main():
	do_twice(print_twice, 'spam')

	print("\n")

	do_four(print, 'hellow, my friend')

def do_twice(f, valor):
	f(valor)
	f(valor)
	
def print_twice(valor):
	print(valor)
	print(valor)

def do_four(f, valor):
    do_twice(f, valor)
    do_twice(f, valor)

main()
