import turtle
import math

def isosceles(t, r, angulo):

    y = r * math.sin(angulo * math.pi / 180)
    t.rt(angulo)
    t.fd(r)
    t.lt(90+angulo)
    t.fd(2*y)
    t.lt(90+angulo)
    t.fd(r)
    t.lt(180-angulo)

def segmentos(t, n, r):

    angulo = 360/n
    for i in range(n):
        isosceles(t, r, angulo/2)
        t.lt(angulo)
    
def movimento(t, n, r):
    segmentos(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd

sam = turtle.Turtle()
movimento(sam, 5, 50)
    
        




        
        
sam =  turtle.Turtle()
sam.color("Green")
sam.speed(1)
triangulo(sam,8, 50)
    
