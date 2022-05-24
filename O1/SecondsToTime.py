print("Enter a number of seconds")

#finner total antall sekunder minutter og timer og henter ut resten
#av å dele totalen på 60 slik at man får riktig tall
totSeconds = int(input())
seconds = totSeconds % 60
totMinutes = totSeconds // 60
minutes = totMinutes % 60
totHoures = totMinutes // 60

#Legger til en 0 forran hvis det kun er et siffer og konverterer int til str
if seconds < 10:
    seconds = "0" + str(seconds)
else:
    seconds = str(seconds)

if minutes < 10:
    minutes = "0" + str(minutes)
else:
    minutes = str(minutes)

if totHoures < 10:
    totHoures = "0" + str(totHoures)
else: 
    totHoures = str(totHoures)

print(totHoures + ":" + minutes + ":" + seconds)