import turtle
from poligono import *

def main():
    sam = turtle.Turtle()
    sam.color("Blue")
    sam.speed(10)
    movimento(sam, -150)
    flor(sam, 7, 60, 60)
    
    sam.color("Red")
    sam.speed(10)
    movimento(sam, 150)
    flor(sam, 25, 100, 80)
    
    sam.color("Green")
    sam.speed(10)
    movimento(sam, 150)
    flor(sam, 14, 70, 50)
    

    
def petala(t, r, angulo):
    for i in range(2):
        t.circle(r,angulo)
        t.lt(180 - angulo)

def flor(t, n, r, angulo):
    for i in range(n):
        petala(t, r, angulo)
        t.lt(360 / n)

def movimento(t, lenght):
    window = turtle.Screen()
    window.bgcolor("Yellow")
    t.pu() 
    t.fd(lenght)
    t.pd() 
    
main()
