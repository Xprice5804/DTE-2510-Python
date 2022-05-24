# Enter the first point with two double values
x1 = float(input("Enter x-coordinate for Point 1: "))
y1 = float(input("Enter y-coordinate for Point 1: "))

# Enter the second point with two double values
x2 = float(input("Enter x-coordinate for Point 2: "))
y2 = float(input("Enter y-coordinate for Point 2: "))
 
# Compute the distance
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
    
print("The distance between the two points is", distance)