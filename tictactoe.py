from tkinter import *
import tkinter as tk
import tkinter.font as font
import random

class LagSpillerrute():
    def __init__(self, frame, P_row, P_column):
        self.P_row = P_row
        self.P_column = P_column
        self.myfont = font.Font(size = 70)
        self.button = Button(frame, text = " ", font=self.myfont, command=TickTacToe.selectSquare)
        #self.button.text = "X"
        self.button.config(height= 1, width= 2)
        self.button.grid(row = P_row, column = P_column)
        
    
    def changeText(self, str):
        self.button.config(text = str)
    
    def getposition(self):
        return [self.P_row, self.P_column]


class TickTacToe:
    def __init__(self):
        window = Tk()
        window.geometry = '600x600'
        window.title = 'Tick Tac Toe'
        self.pressedButtons = [['','',''], ['','',''], ['','','']]
        
        #self.canvas = Canvas(window, width=600, height=600, bg="white")

        self.frame1 = Frame(window)
        self.frame1.grid(row = 3, column = 3)
        self.table = []
        for row in range(3):
            array = []
            self.table.append(array)
            for col in range(3):
                self.myfont = font.Font(size = 70)
                rute = Button(self.frame1, text = " ", font=self.myfont, command = lambda Lrow=row, Lcol=col: self.selectSquare(Lrow,Lcol), height= 1, width= 2)
                rute.grid(row = row, column = col)
                print(rute)
                array.append(rute)
 

        window.mainloop()

    def selectSquare(self, row, col):
        button = self.table[row][col]
        button['text'] = 'X'
        self.pressedButtons[row][col] = 'X'
        self.nextTurn()
        print([row,col])
        return

    def checkWin(self):
        
        for col in range(3):
            if all(s == 'X' for s in self.pressedButtons[col]):
                print("vinner")
                return True
        #for row in range(3):
        #    if all(s == 'X' for s in self.pressedButtons[row][0]):
        #        print("vinner")
        #        return True
        for x in range(3):
            for y in range(3):
                if all(s == 'X' for s in self.pressedButtons[x][y]):
                    print("vunnet")





        return

    def nextTurn(self):
        def choose():
            row = random.randrange(0,3)
            col = random.randrange(0,3)
            if self.pressedButtons[row][col] == 'X' or self.pressedButtons[row][col] == 'O':
                return choose()
            else:
                return [row,col]
        
        place = choose()
        #print(place)
        button = self.table[place[0]][place[1]]
        #print(button)
        button['text'] = 'O'
        self.pressedButtons[place[0]][place[1]] = 'O'

        self.checkWin()
        return
    


TickTacToe()