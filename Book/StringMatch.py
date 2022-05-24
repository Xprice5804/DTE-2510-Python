def main():
    text = input("Enter a text: ")
    pattern = input("Enter a string pattern: ")
    
    index = match(text, pattern)
    if index >= 0:
        print("matched at index", index)
    else:
        print("unmatched") 

# Return the index of the first match. -1 otherwise.
def match(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if isMatched(i, text, pattern):
            return i

    return -1
    
# Test if pattern matches text starting at index i
def isMatched(i, text, pattern):
    for k in range(len(pattern)):
        if pattern[k] != text[i + k]:
            return False
    
    return True

main()