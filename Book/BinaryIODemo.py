import pickle

def main():
    # Open file for writing binary
    output = open("pickle.dat", "wb")
    pickle.dump(45, output)
    pickle.dump(56.6, output) # Write a float 56.6
    pickle.dump("Programming is fun", output)
    pickle.dump([1, 2, 3, 4], output)
    output.close() # Close the output file

    # Open file for reading binary
    inputFile = open("pickle.dat", "rb")
    print(pickle.load(inputFile)) # Read an input
    print(pickle.load(inputFile))
    print(pickle.load(inputFile))
    print(pickle.load(inputFile))
    inputFile.close() # Close the input file

main() # Call the main function
