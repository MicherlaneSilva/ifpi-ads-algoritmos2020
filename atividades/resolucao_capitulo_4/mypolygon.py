import turtle
import math

def main():
    
    bob = turtle.Turtle()
    alice = turtle.Turtle()
    #polygon(alice, length = 60, n = 6)
    #square(bob, length =50)
    circle(bob, 50)
    #arc(bob, 50, 120)
  
def square(t, length):
    
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

def polygon(t, length, n):

    angulo = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angulo)
    turtle.mainloop()

def circle(t, r):

    arc(t, r, 360)

def arc(t, r, angle):
    arc_lenght = 2 * math.pi * r * angle/360
    n = int(arc_lenght / 3) +1
    step_lenght = arc_lenght / n
    step_angle = angle / n
    polyline(t, n, step_lenght, step_angle)

def polyline(t, n, lenght, angle):
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)
    
    
main()


