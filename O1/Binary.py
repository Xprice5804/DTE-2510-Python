print("enter a nubmber between 0 and 15")


def convert():
    number = int(input())
    binary = []
    a = 0
    if 0 < number <= 15:
        while number != 0:
            #finner først ut om resten etter å ha delt med 2 er 1 eller 0 og legger dette til i binary list
            a = number %2
            binary.append(int(a))
            #deler tallet på 2 uten å ha med desimal
            number = number//2
        binary.reverse()
        print(*binary, sep="")
    else:
        print("the number is not between 0 and 15")
        convert()
        return
    #Snur listen baklengs og printer ut alle elementene uten mellomrom

convert()