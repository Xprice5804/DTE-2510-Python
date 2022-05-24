from tkinter import * # Import tkinter
import tkinter.messagebox
from BST import BST 
from BTView import BTView
    
class BSTAnimation:
    def __init__(self, tree):
        window = Tk() # Create a window
        window.title("BSTAnimation") # Set a title
        
        self.width = 200
        self.height = 200
        self.radius = 20
        self.vGap = 50
        self.tree = tree
        self.view = BTView(tree, window, self.width, self.height, 
            self.radius, self.vGap)
        self.view.pack()
        
        frame = Frame(window) # Create and add a frame to window
        frame.pack()
        
        Label(frame, text = "Enter a key").pack(side = LEFT)
        self.key = StringVar()
        Entry(frame, textvariable = self.key, 
            justify = RIGHT).pack(side = LEFT)
        Button(frame, text = "Insert", 
            command = self.insert).pack(side = LEFT)
        Button(frame, text = "Delete", 
            command = self.delete).pack(side = LEFT)
        
        window.mainloop() # Create an event loop


    def insert(self):
        k = int(self.key.get())
        if self.tree.search(k): # key is in the tree already
            tkinter.messagebox.showinfo("Insertion Status", str(k) + 
                                        " is already in the tree")
        else:
            self.tree.insert(k) # Insert a new key
            self.view.delete("tree")
            self.view.displayTree(self.tree.getRoot(), self.width / 2, 
                30, self.width / 4)
    
    def delete(self):
        k = int(self.key.get())
        if not self.tree.search(k): # key is in the tree already
            tkinter.messagebox.showinfo("Deletion Status", str(k) + 
                                        " is not in the tree")
        else:
            self.tree.delete(k) # Delete a key
            self.view.delete("tree")
            self.view.displayTree(self.tree.getRoot(), self.width / 2, 
                30, self.width / 4)

BSTAnimation(BST())
