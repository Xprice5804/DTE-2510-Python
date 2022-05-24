print("please enter a number")
number = int(input())

# Return the reversal of an integer, e.g. reverse(456) returns 654
def reverse(number): 
    #gjør tallet om til en string og bruker en slice som begynner på den siste bokstaven og beveger seg mot starten
    #og gjør deretter stringen over til en intreger igjen
    return int(str(number)[::-1])

# Return true if number is a palindrome
def isPalindrome(number): 
    #er tallet og tallet baklengs det samme så er det et palidrom
    if number == reverse(number):
        return True

if isPalindrome(number):
    print(str(number)+ " is a palidrome")
else:
    print(str(number)+ " is not a palidrome")



