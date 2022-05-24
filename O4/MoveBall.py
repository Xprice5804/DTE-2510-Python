from tkinter import *
import tkinter as tk

class MoveBall:
    def __init__(self):
        window = Tk()
        window.title = 'Move Ball'
        window.geometry = '600x400'

        self.x1 = 10
        self.y1 = 10
        self.x2 = 90
        self.y2 = 90
        self.canvas = Canvas(window, width = 600, height = 350, bg = 'white')
        self.canvas.grid(row =1, column = 1)

        self.ball = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = "red", tags = "circle")

        self.frame1 = Frame(window)
        self.frame1.grid(row = 2, column = 1)
        self.btnUp = Button(self.frame1, text = 'Up', command = self.moveUp)
        self.btnRigth = Button(self.frame1, text = 'Rigth', command = self.moveRigth)
        self.btnLeft = Button(self.frame1, text = 'Left', command = self.moveLeft)
        self.btnDown = Button(self.frame1, text = 'Down', command = self.moveDown)

        self.btnUp.grid(row = 1, column = 1) 
        self.btnRigth.grid(row = 1, column = 2)
        self.btnLeft.grid(row = 1, column = 3)
        self.btnDown.grid(row = 1, column = 4)

        print(self.ball)

        window.mainloop()

    def moveUp(self):
        if self.y1 == 0:
            return
        else:
            self.canvas.delete('circle')
            self.y1 = self.y1 - 10
            self.y2 = self.y2 - 10
            self.ball = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = "red", tags = "circle")

    
    def moveRigth(self):
        if self.x2 == 600:
            return
        else:
            self.canvas.delete('circle')
            self.x1 = self.x1 + 10
            self.x2 = self.x2 + 10
            self.ball = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = "red", tags = "circle")

    def moveLeft(self):
        if self.x1 == 0: 
            return
        else:
            self.canvas.delete('circle')
            self.x1 = self.x1 - 10
            self.x2 = self.x2 - 10
            self.ball = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = "red", tags = "circle")

    
    def moveDown(self):
        if self.y2 == 350:
            return
        else:
            self.canvas.delete('circle')
            self.y1 = self.y1 + 10
            self.y2 = self.y2 + 10
            self.ball = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = "red", tags = "circle")


MoveBall()