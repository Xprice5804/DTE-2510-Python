x = 1 # Global variable
def f1():
    x = 2 # Local variable
    print(x) # Displays 2
  
f1()
print(x) # Displays 1
