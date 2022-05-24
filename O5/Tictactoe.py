from tkinter import *
"""[summary]
    
class TicTacToe:
    def __init__ (self):
        self.window = Tk()
        self.window.title("Tic Tac Toe")
        Cell()
        #frame1 = Cell()

class Cell():
    def __init__(self):
        self.ImgEmpty = PhotoImage(file="empty.gif")
        self.ImgX = PhotoImage(file="x.gif")
        self.ImgO = PhotoImage(file="o.gif")
        self.label = Label(TicTacToe.window, image = self.ImgEmpty)
        self.label.grid(row=1, column=1)
       
        # Bind with <Button-1> event
        self.label.bind("<Button-1>", self.processMouseEvent)
       
        TicTacToe.window.mainloop() # Create an event loop

    def processMouseEvent(self, event):
        print("clicked at", event.x, event.y)
        print("Position in the screen", event.x_root, event.y_root)
        print("Which button is clicked? ", event.num)


        
TicTacToe()
"""
class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic Tac Toe")
        #self.window.bind("<Button-1>", self.processMouseEvent)
        self.ImgEmpty = PhotoImage(file="empty.gif")
        self.ImgX = PhotoImage(file="x.gif")
        self.ImgO = PhotoImage(file="o.gif")
        
        self.label1 = Label(self.window, image = self.ImgEmpty)
        self.label1.grid(row=1, column=1)
        self.label1.bind("<Button-1>", lambda event, a = 1: self.processMouseEvent(event, a))
        
        self.label2 = Label(self.window, image = self.ImgEmpty)
        self.label2.grid(row=1, column=2)
        self.label2.bind("<Button-1>", lambda event, a = 2: self.processMouseEvent(event, a))
        
        self.label3 = Label(self.window, image = self.ImgEmpty)
        self.label3.grid(row=1, column=3)
        self.label3.bind("<Button-1>", lambda event, a = 3: self.processMouseEvent(event, a))
        
        self.label4 = Label(self.window, image = self.ImgEmpty)
        self.label4.grid(row=2, column=1)
        self.label4.bind("<Button-1>", lambda event, a = 4: self.processMouseEvent(event, a))
        
        self.label5 = Label(self.window, image = self.ImgEmpty)
        self.label5.grid(row=2, column=2)
        self.label5.bind("<Button-1>", lambda event, a = 5: self.processMouseEvent(event, a))
        
        self.label6 = Label(self.window, image = self.ImgEmpty)
        self.label6.grid(row=2, column=3)
        self.label6.bind("<Button-1>", lambda event, a = 6: self.processMouseEvent(event, a))
        
        self.label7 = Label(self.window, image = self.ImgEmpty)
        self.label7.grid(row=3, column=1)
        self.label7.bind("<Button-1>", lambda event, a = 7: self.processMouseEvent(event, a))
        
        self.label8 = Label(self.window, image = self.ImgEmpty)
        self.label8.grid(row=3, column=2)
        self.label8.bind("<Button-1>", lambda event, a = 8: self.processMouseEvent(event, a))
        
        self.label9 = Label(self.window, image = self.ImgEmpty)
        self.label9.grid(row=3, column=3)
        self.label9.bind("<Button-1>", lambda event, a = 9: self.processMouseEvent(event, a))
        
        self.window.mainloop()
    
    def processMouseEvent(self, event, button):
        print(event)
        print(button)
        
        
    
        
TicTacToe()
