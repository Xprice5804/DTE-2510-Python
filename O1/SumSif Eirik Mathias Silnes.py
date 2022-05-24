print('Write a number between 0 and 1000')
sum = 0 
num = int(input())

#skjekker om tallet er mellelom 1 og 1000
if 1 <= num <= 1000: 
    length = len(str(num))
    #summerer sammen siffer i en while loop
    while length > 0:
        sum = sum + (num % 10)
        num = num // 10
        length -= 1
    print(sum)
else:
    print('The number is not between 0 and 1000')