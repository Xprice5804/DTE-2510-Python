from tkinter import *

turn = True

class Tic:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic Tac Toe")
        self.__turn = True
        self.listofStuff = []
        
        for i in range(3):
            for j in range(3):
                self.listofStuff.append(Cell(self.window,i,j))
        
        
        self.window.mainloop()
    
    def getTurn(self):
        return self.__turn
    
    def setTurn(self, turn):
        self.__turn = turn



class Cell:
    def __init__(self, frame, x, y):
        self.x = x
        self.y = y
        self.ImgEmpty = PhotoImage(file="empty.gif")
        self.ImgX = PhotoImage(file="x.gif")
        self.ImgO = PhotoImage(file="o.gif")
        self.frame = frame
        
        self.label1 = Label(frame, image = self.ImgEmpty)
        self.label1.grid(row=x, column=y)
        self.label1.bind("<Button-1>", lambda event, a = x, b = y: self.processMouseEvent(event, a, b))
        
    def processMouseEvent(self, event, a, b):
        print([a,b])
        if game.getTurn():
            self.changeX()
        else:
            self.changeO()
        
        return [a,b]
    
    def changeX(self):
        self.label1.configure(image = self.ImgX)
        
    def changeO(self):
        self.label1.configure(image = self.ImgO)
        
game = Tic()