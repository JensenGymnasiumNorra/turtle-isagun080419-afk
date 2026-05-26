"""
Alla kommandon för turtle finns i filen kommandon.md
Nu ska du göra en smiley. Börja med att göra tre variabler: storlek på huvudet, storlek på ögonen och storlek på munnen.
Rita en smiley med turtle och använd variablerna så att smileyn lätt kan ändras.


"""
import turtle

huvud=100
ögon=30
mun=40

t = turtle.Turtle()

t.penup()
t.goto(0, -huvud)
t.pendown()
t.circle(huvud)

t.penup()
t.goto(-huvud/3, huvud/4)
t.pendown()
t.circle(ögon)


turtle.done()