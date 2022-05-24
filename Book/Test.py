# Michelle Liang
# Section -B3
# Email - michelle.liang36@gatech.edu
# Collaboration statement - I did not collaborate with anyone on this assignment and used my own brain power.

def abbreviator(astr):
    newstr = ""
    # Split the string into substrings using space as delimiters
    items = astr.split()
    for item in items:
        # add the letter that is captial
        if len(item) > 0 and item[0].isupper():
            newstr += item[0]   
        # add the numbers
        elif item.isdigit():
            newstr += item                   
    return newstr

# big-O for abbreviator function
# the astr.split() takes O(n) times
# the for loop takes O(n) times
# therefore the total time is O(n)
 
##print(abbreviator("Chet jus,t sTole my gir34l Again!"))
##print(abbreviator("The Life of Pablo"))
##print(abbreviator("3,0 Rock"))
##print(abbreviator("13 2,0 Rock"))
##print(abbreviator("aHappy Camper"))

def union(list1, list2):
    # merge two lists
    merge = list1 + list2
    # sort the new list 
    merge.sort()
    # remove any duplicates
    newlist = merge[:1]
    for number in merge:
        if number != newlist[-1]:
            newlist.append(number)
    return newlist

#Big O for the union function:
#It takes O(n) time to combine to lists
#It takes O(nlogn) time to sort the combined list using merge sort
#It takes O(n) time to remove duplicates in the sorted list
#So, the total time is O(nlogn) for the union function. 

##a = [1,3,2.0]
##b = [4,2,5, 3.0]
##c = union(a,b)
##print(c)
##d = [7,5,3,5]
##e = [79.3,5.0,2,6]
##f = union(d,e)
##print(f)

def tupleMagic(aList):
    for i in range(len(aList)):
        e = aList[i]
        tempList = list(e)
        sum = 0.0
        for number in e:
            sum += number
        tempList.insert(0, sum / len(e))
        aList[i] = tuple(tempList)

# Big-O for the tupleMagic function
# let n be the total number of elements in all tuples since each element is added to the sum only once
# the overall time is O(n). 
           
##aList = [(1,1,1), (1,2,4,5,6), (2,1,3)]
##tupleMagic(aList)
##print(aList)

def reverseMultiTable(n):
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            print("{0:<6d}".format(i * j), end = "")
        print()

# Big-O for reverseMultiTable function
# The first for loop takes O(n) time
# The second nested for loop takes O(n) time
# Therefore the total time O(n^2). 
        
##reverseMultiTable(0)
##reverseMultiTable(2)
##reverseMultiTable(3)
##reverseMultiTable(5)
##reverseMultiTable(7)
##reverseMultiTable(9)
    
def charCount(s):
    aDict = {}
    first = True
    for ch in s:
        if ch == ' ':
            if first:
                print("First Space")
                first = False
            else:
                print("ANOTHA ONE")
        elif ch in aDict:  
            aDict[ch] += 1
        else:
            aDict[ch] = 1              
    return aDict

# The Big-O for charCount function
# the for loop takes O(n) times
# therefore the total is O(n).

##print(charCount("Mi ch el le ! !"))
##print(charCount(""))
##print(charCount("hello"))
##print(charCount("Yung Coco Butter"))
##print(charCount("Yung Coco Butter I am "))
##print(charCount("Finals is coming up! "))

# This helper function is used in chetify
# The function returns True if character ch is a punctuation
def isPuctuation(ch):
    puctuation = "!\"#$%&'()*,./:;<=>?@[\]^`{|}~" 
    return ch in puctuation
 
# This helper function is used in chetify
# Return a new string that inserts the space before a punctuation in s
# example, insertSpaceBeforePunctuation("we, like.") returns "we , like ."
def insertSpaceBeforePunctuation(s):
    result = "" # result is the new string with a space before each punctuation
    for ch in s:
        if isPuctuation(ch):
            result += ' ' + ch # add a space before a punctuation
        else:
            result += ch
    return result
 
# This helper function is used in chetify
# Return a new string that removes the space before a punctuation in s
# example, removeSpaceBeforePunctuation("we , about .") returns "we, about."
def removeSpaceBeforePunctuation(s):
    # Remove the space before a punctuation in s
    result = "" # result is the new string with a space removed from a punctuation
    for i in range(len(s)):
        if s[i] == ' ' and i + 1 < len(s) and isPuctuation(s[i + 1]):
            pass # do nothing
        else:
            result += s[i] # Copy the character to text
    return result
       
def chetify(filename):
    input = open(filename, "r")
    text = input.read()
    # Insert a space before a punctuation in text so that string such as "like." will be "like ."
    text = insertSpaceBeforePunctuation(text)
    aDict = {" Young ": " Yung ", " you ": " we ", " yea ": " yee ", " like ": " about "}
    for key in aDict:
        text = text.replace(key, aDict[key])
    # Remove the space before a punctuation in text
    text = removeSpaceBeforePunctuation(text)
    input.close()
    output = open("chetify.txt", "w")
    output.write(text)
    output.close()
   
chetify("sample.txt")
 
# The Big-O for chetify function
# The insertSpaceBeforePunctuation(text) function takes O(n) time
# There are four keys in the dictionary aDict, so the replace method is invoked 4 times.
# The test.replace takes O(n) time. So the loop to replace the word takes 4 * O(n) time.
# The removeSpaceBeforePunctuation(text) function takes O(n) time
# So, overall, the chetify function takes O(n) time.


# The Big-O explanation is inserted after each function. 
    
    

