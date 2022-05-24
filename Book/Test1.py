import re

regex = "b.*"
match1 = re.match(regex, 'ab\n\rd')

if match1 != None:
    print(" valid ")
    print("start position of the matched text is " + 
        str(match1.start()))
    print("start and end position of the matched text is " +
        str(match1.span()))
else:
    print(" is not a valid SSN")