from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title = ("Classes")
root.geometry("900x500")

gui_elements = ["Labels", "Dropdown", "Button"]
dropdown = ttk.Combobox(root, state = "readonly", values = gui_elements )
dropdown.pack()

class CreateElements:
    def __init__ (self):
        print("This is CreateElements class.")
        
    def create_label(self):
        label = Label(root, text = "A new label is been created using the class", fg = "red")
        label.pack()
        
    def create_button(self):
        class_btn = Button(root, text = "Button", command = self.message)
        class_btn.pack(padx = 20, pady = 10)
        
    def create_dropdown(self):
        value = [1, 2, 3, 4]
        class_dropdown = ttk.Combobox(root, state = "readonly", values = value)
        class_dropdown.pack()
        
    def choose(self):
        global dropdown
        element = dropdown.get()
        if(element == "Label"):
            self.create_label()
        elif(element == "Button"):
            self.create_button()
        elif(element == "Dropdown"):
            self.create_dropdown()
            
def message(self):
    messagebox.showinfo("showinfo", "You clicked the button created using the class")
    
obj_of_CreateElements = CreateElements()

btn = Button(root, text = "Create Elements", command = obj_of_CreateElements.choose)
btn.pack(padx = 20, pady = 10)

root.mainloop()