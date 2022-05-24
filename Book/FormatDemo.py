import math

# Display the header of the table 
print(format("Degrees", "<10s"), format("Radians", "<10s"),
    format("Sine", "<10s"), format("Cosine", "<10s"), 
    format("Tangent", "<10s"))

# Display values for 30 degrees
degrees = 30
radians = math.radians(degrees)
print(format(degrees, "<10d"), format(radians, "<10.4f"),
    format(math.sin(radians), "<10.4f"),  
    format(math.cos(radians), "<10.4f"),
    format(math.tan(radians), "<10.4f"))

# Display values for 60 degrees
degrees = 60
radians = math.radians(degrees)
print(format(degrees, "<10d"), format(radians, "<10.4f"),
    format(math.sin(radians), "<10.4f"),  
    format(math.cos(radians), "<10.4f"),
    format(math.tan(radians), "<10.4f"))