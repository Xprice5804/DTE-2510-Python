globalVar = 1
def f1():
    localVar = 2
    print(globalVar)
    print(localVar)
   
f1()
print(globalVar)
print(localVar) # Out of scope, so this gives an error
