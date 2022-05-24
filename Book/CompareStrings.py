s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if s2 < s1:
    s1, s2 = s2, s1

print("The two strings are in this order:", s1, s2)