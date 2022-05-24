from calendar import monthrange

print('Please enter a month (1=january 2=february and so on)')
month = int(input())
print('please enter a year')
year = int(input())

numberDays = monthrange(year, month)[1]

print(numberDays)