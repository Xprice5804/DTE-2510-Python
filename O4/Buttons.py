from tkinter import*

class RButtonTest:
    def __init__(self):
        window = Tk() #Lager et vindu
        window.geometry("400x100")
        top = Frame(window)
        top.pack()
        self.middle = Frame(window)
        self.middle.pack()
        bottom = Frame(window)
        bottom.pack()
        
        #lager en farge variabel
        self.color = StringVar()
        
        #Lager alle radio buttons 
        rbtRed = Radiobutton(top, text = 'Red', variable = self.color, value = 'Red', command = self.processColor)
        rbtYellow = Radiobutton(top, text = 'Yellow', variable = self.color, value = 'Yellow', command = self.processColor)
        rbtWhite = Radiobutton(top, text = 'White', variable = self.color, value = 'White', command = self.processColor)
        rbtGray = Radiobutton(top, text = 'Gray', variable = self.color, value = 'Gray', command = self.processColor)
        rbtGreen = Radiobutton(top, text = 'Green', variable = self.color, value = 'Green', command = self.processColor)
        
        #plaserer alle radio buttons på en linje med grid
        rbtRed.grid(row = 1, column = 1)
        rbtYellow.grid(row = 1, column = 2)
        rbtWhite.grid(row = 1, column = 3)
        rbtGray.grid(row = 1, column = 4)
        rbtGreen.grid(row = 1, column = 5)
        
        #plaserer teksten inne i en label i den hensik å kunne fylle hele tomrommet og i tillegg bruke .place funksjonen
        self.label = Label(self.middle, bg = 'Yellow') 
        self.label2 = Label(self.label, text = 'Welcome', font = ("Arial", 24), bg = 'Yellow')
        self.label.pack(fill = BOTH, expand = 1)
        self.label2.place(x = 130, y = 0)

        #Lager høyre og venstre knapp
        self.btRight = Button(bottom, text ='=>', command = self.processRight, font = ("Arial", 18))
        self.btLeft = Button(bottom, text = '<=', command = self.processLeft, font = ("Arial", 18))
        self.btRight.grid(row = 1, column = 2)
        self.btLeft.grid(row = 1, column = 1)


        window.mainloop()

    #flytter teksten til høyre med 20 px
    def processRight (self):
        self.label2.place(x = self.label2.winfo_x()+ 20)
    
    #flytter teksten til venstre med 20px
    def processLeft (self):
        self.label2.place(x = self.label2.winfo_x()- 20)
    
    #endrer fargen på bakrunnen
    def processColor (self):
        self.label['bg'] = self.color.get()
        self.label2['bg'] = self.color.get()

RButtonTest()
        