import turtle

x1 = float(input("Enter the center x-coordinate of a circle: "))
y1 = float(input("Enter the center y-coordinate of a circle: "))
radius = float(input("Enter the radius of the circle: "))
x2 = float(input("Enter a point x-coordinate: "))
y2 = float(input("Enter a point y-coordinate: "))

# Draw the circle
turtle.penup() # Pull the pen up
turtle.goto(x1, y1 - radius)
turtle.pendown() # Pull the pen down
turtle.circle(radius)

# Draw the point
turtle.penup() # Pull the pen up
turtle.goto(x2, y2)
turtle.pendown() # Pull the pen down
turtle.dot(6, "red")

# Display the status
turtle.penup() # Pull the pen up
turtle.goto(x1 - 70, y1 - radius - 20)
turtle.pendown() 

d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
if d <= radius:
    turtle.write("The point is inside the circle") 
else:
    turtle.write("The point is outside the circle") 

turtle.hideturtle()

turtle.done() 