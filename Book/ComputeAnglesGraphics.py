import math

x1 = float(input("Enter x-coordinate for Point 1: "))
y1 = float(input("Enter y-coordinate for Point 1: "))
x2 = float(input("Enter x-coordinate for Point 2: "))
y2 = float(input("Enter y-coordinate for Point 2: "))
x3 = float(input("Enter x-coordinate for Point 3: "))
y3 = float(input("Enter y-coordinate for Point 3: "))
 
a = math.hypot(x2 - x3, y2 - y3)
b = math.hypot(x1 - x3, y1 - y3)
c = math.hypot(x1 - x2, y1 - y2)

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

import turtle

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()

turtle.goto(x2, y2)
turtle.write(round(B, 2))
turtle.goto(x3, y3)
turtle.write(round(C, 2))
turtle.goto(x1, y1)
turtle.write(round(A, 2))

turtle.done()
