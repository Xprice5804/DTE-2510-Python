print('Enter your weigth in KG:')
#tvinger python til å kun bruke float for å ikke error på matten
weigth = float(input()) 
print('Enter your height in meters:')
height = float(input())

bmi = weigth / height ** 2
bmi = round(bmi, 1) #avrunde svaret til en desimal
print('Your Body mass index is: {bmi}')