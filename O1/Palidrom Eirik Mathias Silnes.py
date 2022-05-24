print('enter a three didgit number')
num = int(input())
num1 = num % 10
num2 = num // 100

#skjekker om det er et tresifret nummer
if len(str(num)) == 3:
    #hvis første og siste siffer er dt samme så er det et palidrom hvis tallet er tre siffer langt
    if num1 == num2:
        print('IT IS A PALIDROME')
    else:
        print('It is not a palidrome')
else:
    print('the number must be three didgits')