from GCDFunction import gcd # Import the module

# Prompt the user to enter two integers
n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))

print("The greatest common divisor for", n1,
    "and", n2, "is", gcd(n1, n2))
