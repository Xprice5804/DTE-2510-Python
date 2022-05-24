from tkinter import *
import tkinter as tk

#celsius = int(input('Enter a celsius temperature'))

class TemperatureConverter:
    

    def __init__(self):
        self.window = Tk()
        self.window.title('Convert from Celsius to Fahrenheit')
        self.InputG = tk.StringVar()

        LabelInp = Label(self.window, text = 'Celsius:').grid(row = 1, column = 1)
        CelsiusInp = Entry(self.window, textvariable = self.InputG).grid(row = 1, column = 2, columnspan = 3, padx = 5, pady = 5)
        ConvertBtn = Button(self.window, text = 'Convert', command = self.convertCF).grid(row = 3, column = 5, sticky =E)
        self.AnswerLb = Label(self.window, text = 'Fahrenheit:')
        self.AnswerLb.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 5)
        self.window.mainloop()

    def convertCF(self):
        fahrenheit = (int(self.InputG.get()) * 1.8) +32
        fahrenheitStr = str(fahrenheit)
        self.AnswerLb['text'] = 'Fahrenheit: ' + fahrenheitStr
        print(self.AnswerLb)

TemperatureConverter()