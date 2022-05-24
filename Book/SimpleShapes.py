import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-170, -25)
turtle.pendown()
turtle.circle(30, steps = 3) # Draw a triangle

turtle.penup()
turtle.goto(-85, -25)
turtle.pendown()
turtle.circle(30, steps = 4) # Draw a square

turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(30, steps = 5) # Draw a pentagon

turtle.penup()
turtle.goto(85, -25)
turtle.pendown()
turtle.circle(30, steps = 6) # Draw a hexagon

turtle.penup()
turtle.goto(170, -25)
turtle.pendown()
turtle.circle(30) # Draw a circle

turtle.done() 