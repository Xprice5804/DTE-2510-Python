print("please enter a genome")
genome = str(input())
strSplit = ["TAG", "TAA", "TGA"]

list1 = genome.split("ATG")

for x in list1:
    #Lager en index verdi i tilfelle str endres i neste loop
    index = list1.index(x) 
    for y in strSplit:
        #fjern alt som er bak "TAG", "TAA" og "TGA" for å markere slutt på genet
        list1[index] = list1[index].split(y, 1)[0]

#Fjern alt som ikke kan deles på tre
for x in list1:
    if len(x) % 3 is not 0:
        list1.remove(x)

#skriver ut svaret med en ny linje for hvert gen
if len(list1) > 0:
    print("These genes was found")
    print(*list1, sep = "\n")
else:
    print("no gene found")