from tkinter import * # Import tkinter

window = Tk() # Create a root window
label = Label(window, text = "Welcome to Python") # Create a label
button = Button(window, text = "Click Me") # Create a button
label.pack() # Display the label in the window
button.pack() # Display the button in the window

window.mainloop() # Create an event loop