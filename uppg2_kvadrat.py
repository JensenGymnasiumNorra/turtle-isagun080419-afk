"""
Alla kommandon för turtle finns i filen kommandon.md
Skapa en ny turtle
Rita en kvadrat med .forward och .right
Lyft upp din turtles penna genom att använda .penup()
Flytta nu till en annan punkt (x,y) genom att använda .goto(x,y)
Rita en till kvadrat med hjälp av .goto(x,y) som inte överlappar med den första kvadraten.
"""
import turtle

t = turtle.Turtle()

def kvadrat():
    for i in range(4):
        t.forward(10)
        t.left(90)

kvadrat()
t.penup()
t.goto (30,70)
t.pendown()
kvadrat()

turtle.done()