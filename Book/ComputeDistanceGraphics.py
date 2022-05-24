import turtle

# Prompt the user for inputing two points
x1 = float(input("Enter x-coordinate for Point 1: "))
y1 = float(input("Enter y-coordinate for Point 1: "))
x2 = float(input("Enter x-coordinate for Point 2: "))
y2 = float(input("Enter y-coordinate for Point 2: "))
              
# Compute the distance
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Display two points and the connecting line
turtle.penup()
turtle.goto(x1, y1) # Move to (x1, y1)
turtle.pendown()
turtle.write("Point 1") 
turtle.goto(x2, y2) # draw a line to (x2, y2)
turtle.write("Point 2")

# Move to the center point of the line
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2) 
turtle.write(distance)

turtle.done() 