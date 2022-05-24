import random

#Total mengde punkter som skal lages og en verdi til å registrere treff
TotPoints= 1000000
numberOfHits= 0
 
for x in range(TotPoints):
 
    #generer et tilfeldig tall mellom -1 og 1 og regner ut avstanden til sentrum av sirkelen
    #ved hjelp av pytagoras læresetning
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    dist = x**2 + y**2
 
    # radiusen er satt til 1 så ser om punktet er lenger vekk enn 1 fra sentrum, hvis ikke registrer treff
    if dist <= 1:
        numberOfHits+= 1
 
    #Bruker mengden dreff til å bergne PI
    pi = 4* numberOfHits/ TotPoints
 
print("Pi =", pi)