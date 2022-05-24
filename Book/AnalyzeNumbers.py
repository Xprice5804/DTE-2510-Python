NUMBER_OF_ELEMENTS = 3 # For simplicity, use 3 instead of 100
numbers = [] # Create an empty list
sum = 0

for i in range(NUMBER_OF_ELEMENTS): 
    value = float(input("Enter a new number: "))
    numbers.append(value) # Append value to numbers list
    sum += value
    
average = sum / NUMBER_OF_ELEMENTS

count = 0 # The number of elements above average
for i in range(NUMBER_OF_ELEMENTS): 
    if numbers[i] > average:
        count += 1

print("Average is", average)
print("Number of elements above the average is", count)
