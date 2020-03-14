import turtle

def main():
    bob = turtle.Turtle()
    tamanho = 50
    lados = 8
    square(bob, tamanho, lados)
    
def square(t, length, n):

    angulo = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angulo)
    turtle.mainloop()

main()
