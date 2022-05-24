import turtle 
import time

#Lager en stor 
turtle.begin_fill() 
turtle.color("yellow")
turtle.circle(60) 
turtle.end_fill() 

#Lager to øyne med .dot funksjonen
turtle.penup()
turtle.goto(-40, 70)
turtle.pendown()
turtle.dot(10, "black")

turtle.penup()
turtle.goto(40, 70)
turtle.pendown()
turtle.dot(10, "black")

#Lager et smil i en loop ved å vende turtle mens den beveger seg fremover
turtle.penup()
turtle.color("black")
turtle.goto(30, 40)
turtle.right(90)
turtle.pensize(3)
turtle.pendown()
turtle.speed(10)
for x in range(90):
    turtle.forward(1)
    turtle.right(2)
turtle.penup()
turtle.done

#Venter litt så man kan beundre resulatatet
time.sleep(10)