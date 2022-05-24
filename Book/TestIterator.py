from LinkedList import LinkedList

list = LinkedList() # Create a linked list
list.add(1) 
list.add(2) 
list.add(3) 
list.add(-3) 

for e in list:
    print(e, end = ' ')
print()

iterator = iter(list) # Create an iterator
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))