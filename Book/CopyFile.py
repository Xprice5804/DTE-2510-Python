import os.path
import sys

def main():
    # Prompt the user to enter filenames
    f1 = input("Enter a source file: ").strip()
    f2 = input("Enter a target file: ").strip()

    # Check if target file exists
    if os.path.isfile(f2):
        print(f2 + " already exists")
        sys.exit()

    # Open files for input and output
    inputFile = open(f1, "r")
    outputFile = open(f2, "w")

    # Copy from input file to output file
    countLines = countChars = 0
    for line in inputFile:
        countLines += 1
        countChars += len(line)
        outputFile.write(line) # Write line to output
    print(countLines, "lines and", countChars, "chars copied")

    inputFile.close()  # Close the input file
    outputFile.close() # Close the output file

main() # Call the main function
