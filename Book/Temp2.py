class A:
    # Construct a circle object 
    def __init__(self, k = 1):
        self.__k = k

    def __add__(self, a2):
        return A(self.__k + a2.__k)
    
    def __str__(self):
        return str(self.__k)

a1 = A(4)
a2 = A(5)
print(a1 + a2)