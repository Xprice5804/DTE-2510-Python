def main():
    # Prompt the user to enter a hex number
    hex = input("Enter a hex number: ").rstrip()

    decimal = hexToDecimal(hex.upper())
    if decimal == None:
        print("Incorrect hex number")
    else:
        print("The decimal value for hex number", 
            hex, "is", decimal) 

def hexToDecimal(hex):
    decimalValue = 0
    for hexChar in hex:
        if 'A' <= hexChar <= 'F' or '0' <= hexChar <= '9':
            decimalValue = decimalValue * 16 + \
                hexChar2Dec(hexChar)
        else:
            return None

    return decimalValue

def hexChar2Dec(ch):
    if 'A' <= ch <= 'F':
        return 10 + ord(ch) - ord('A')
    else:
        return ord(ch) - ord('0')

main() # Call the main function