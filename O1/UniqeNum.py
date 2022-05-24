print("Please enter numbers with one space in between them")
stringOfNum = str(input())
listOfNum = stringOfNum.split(" ")
listOfUniqe = []

#Legger til et tall i listen listOfUniqe hvis det ikke finnes der fra før av
for x in listOfNum:
    listOfUniqe.append(x) if x not in listOfUniqe else listOfUniqe

#skriv ut svaret med et mellomrom mellom hvert tall
print("These numbers are the uniqe ones:")
print(*listOfUniqe, sep = " ")

