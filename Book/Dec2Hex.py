# Prompt the user to enter a decimal integer
decimal = int(input("Enter a decimal integer: "))

# Convert decimal to hex
hex = ""
while decimal != 0:
    hexValue = decimal % 16
    
    # Convert a decimal value to a hex digit 
    if 0 <= hexValue <= 9:
        hexChar = chr(hexValue + ord('0')) 
    else:
        hexChar = chr(hexValue - 10 + ord('A'))
       
    hex = hexChar + hex
    decimal = decimal // 16

print("The hex number is", hex)