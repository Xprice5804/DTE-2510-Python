def getMatrix(): 
    matrix = [] # Create an empty list

    numberOfRows = int(input("Enter the number of rows: "))
    for row in range(numberOfRows): 
        s = input("Enter row " + str(row) + ": ")
        matrix.append([float(x) for x in s.split()])  

    return matrix

def accumulate(m):
    total = 0
    for row in m:
        total += sum(row) # Get the total in the row

    return total

def main():
    m = getMatrix() # Get an list
    print(m)

    # Display sum of elements
    print("\nSum of all elements is", accumulate(m))

main() # Invoke main function
