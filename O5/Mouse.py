from tkinter import *

class MouseKeyEventDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Event Demo") # Set a title
        label = Label(window, text = "I am a label")
        label.pack()
       
        # Bind with <Button-1> event
        label.bind("<Button-1>", self.processMouseEvent)
       
        window.mainloop() # Create an event loop

    def processMouseEvent(self, event):
        print("clicked at", event.x, event.y)
        print("Position in the screen", event.x_root, event.y_root)
        print("Which button is clicked? ", event.num)
   
MouseKeyEventDemo() # Create GUI