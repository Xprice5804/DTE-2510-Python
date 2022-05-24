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
    i = len(pattern) - 1
    while i < len(text):
        k = i
        j = len(pattern) - 1
        while j >= 0:
            if text[k] == pattern[j]:
                k -= 1
                j -= 1
            else:
                break
        
        if j < 0:
            return i - len(pattern) + 1 # A match found
        
        u = findLastIndex(text[k], j - 1, pattern)
        if u >= 0: # text[k] is in the remaining part of the pattern
            i = k + len(pattern) - 1 - u
        else: # text[k] is not in the remaining part of the pattern
            i = k + len(pattern)

    return -1
    
# Return the index of the last element in pattern[0 .. j] 
# that matches ch. -1 otherwise.
def findLastIndex(ch, j, pattern):
    for k in range(j, -1, -1):
        if ch == pattern[k]:
            return k
        
    return -1

main()
