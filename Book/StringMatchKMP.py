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
    f = getFailure(pattern)
    i = 0 # Index on text
    k = 0 # Index on pattern
    while i < len(text):
        if text[i] == pattern[k]:
            if k == len(pattern) - 1:
                return i - len(pattern) + 1 # pattern matched
            i += 1 # Compare the next pair of characters
            k += 1
        else:
            if k > 0:
                k = f[k - 1] # Matching prefix position
            else:
                i += 1 # No prefix
    
    return -1
    
# Compute failure function
def getFailure(pattern):
    fail = len(pattern) * [0]
    i = 1
    k = 0
    while i < len(pattern):
        if pattern[i] == pattern[k]:
            fail[i] = k + 1
            i += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            i += 1
    
    return fail

main()
