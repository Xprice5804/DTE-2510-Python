
class EQ:
    def __init__(self, queens = 8 * [-1]):
        self.Queens = queens
    
    def get(self, i):
        return self.Queens[i]
    
    def set(self, i, j):
        self.Queens[i] = j
   
    def isSolved(self):
        i = 0
        for x in self.Queens:
            b = 0
            for a in range(i - 1, -1, -1):
                b = b+1
                if (x == self.Queens[a]
                    or x-b == self.Queens[a] 
                    or x+b == self.Queens[a]):
                    return False
            i = i+1
        return True

    def printBoard(self):
        for a in range(0,8):
            b = '|'
            for x in self.Queens:
                if x == a:
                    b = b + 'X|'
                else:
                    b = b + ' |'
            print(b)
                


def main():

    board1 = EQ()

    board1.set(0, 2)

    board1.set(1, 4)

    board1.set(2, 7)

    board1.set(3, 1)

    board1.set(4, 0)

    board1.set(5, 3)

    board1.set(6, 6)

    board1.set(7, 5)

    print("Is board1 a correct eight queen placement?",

        board1.isSolved())

 

    board2 = EQ([0, 4, 7, 5, 2, 6, 1, 3])

    if board2.isSolved():

        print("Eight queens are placed correctly in board2")

        board2.printBoard()

    else:

        print("Eight queens are placed incorrectly in board2")
        
main()