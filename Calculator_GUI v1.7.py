from tkinter import *

class Buttons_Class:
    def __init__(self, parent):

        col = 0
        rows = 2
        PY = 20
        PX = 20

        self.display = StringVar()
        
        e = Entry(root, textvariable = display).grid(row = 0, column = 0, columnspan = 4, rowspan = 2, sticky = N+E+W+S)
        
        for key in ("7", "8", "9","C","CE", "4", "5", "6", "/", "*",
                         "1", "2", "3", "+", "-", "0", ".", "="):
            Calculator_Buttons = Button(parent, text = key, command = onClick, pady = PY, padx = PX).grid(row = rows, column = col, sticky = N+E+W+S)
            col = col + 1
            if col > 4:
                rows = rows +1
                col = 0
        return Calculator_Buttons


             

    def onClick(self, key):
        self.display.delete(0, END)
        self.display.insert(END, key)

        

if __name__ == "__main__":
    root = Tk()
    calculator = Buttons_Class(root)
    root.mainloop()

            
            
