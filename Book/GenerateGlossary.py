def main():
    # Open file for input
    inputFile = open("C:\\liangcentral\\python2eREVEL\\x.txt", "r")
    output = open("C:\\liangcentral\\python2eREVEL\\y1.txt", "w")
    
    for line in inputFile:
        line = line.strip()
        
        if line.startswith("Chapter"):
            items = line.split()
            chapterNo = items[1] 
        elif line.startswith("*"):
            items = line.split("@")
            key = items[0][1:].strip()
            description = items[1].strip()
            while description[0] == '?':
                description = description[1 :].strip()
                
#            print(str(chapterNo) + "@" + key + "@" + description + "\r\n")
            output.write(str(chapterNo) + "@" + key + "@" + description + "\r\n")
    
    inputFile.close() # Close the input file
    output.close() # Close the input file

main() # Call the main function