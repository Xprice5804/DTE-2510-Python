from tkinter import * # Import tkinter

class ComboBoxDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Combo Box Demo") # Set title
        
        # Create PhotoImage objects
        self.caImage = PhotoImage(file = "image/ca.gif")
        self.cnImage = PhotoImage(file = "image/china.gif")
        self.usImage = PhotoImage(file = "image/us.gif")
        self.ukImage = PhotoImage(file = "image/uk.gif")

        # Create a combo box to select a country
        var = StringVar()
        var.set("Canada") # initial value
        comboBox = OptionMenu(window, var, "Canada", "China", "US", 
            "UK", command = self.processSelection).pack(fill = BOTH)

        # Create a canvas to display image
        self.canvas = Canvas(window)
        self.canvas.create_image(100, 50, image = self.caImage, 
                                 tag = "image")
        self.canvas.pack()
        
        window.mainloop() # Create an event loop
        
    # Display image for selected country
    def processSelection(self, selectedItem):
        self.canvas.delete("image"); 
        if selectedItem == "Canada":
            self.canvas.create_image(100, 50, image = self.caImage, 
                                     tag = "image")
        elif selectedItem == "China":
            self.canvas.create_image(100, 50, image = self.cnImage,
                                     tag = "image")
        elif selectedItem == "US":
            self.canvas.create_image(100, 50, image = self.usImage,
                                     tag = "image")
        elif selectedItem == "UK":
            self.canvas.create_image(100, 50, image = self.ukImage,
                                     tag = "image")

ComboBoxDemo() # Create GUI 