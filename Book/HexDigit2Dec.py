import sys

hexDigit = input("Enter a hex digit: ").upper()

# Check if the hex digit has exactly one character
if len(hexDigit) != 1:
    print("You must enter exactly one character")
    sys.exit()
        
# Display decimal value for the hex digit
if hexDigit <= 'F' and hexDigit >= 'A':
    value = ord(hexDigit) - ord('A') + 10
    print("The decimal value for hex digit", hexDigit, "is", value)
elif hexDigit.isdigit():
    print("The decimal value for hex digit", hexDigit, "is", hexDigit)
else:
    print(hexDigit, "is an invalid input")