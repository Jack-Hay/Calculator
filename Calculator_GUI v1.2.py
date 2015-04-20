# GUI Only
#Jack Hay 2/04/15
from tkinter import *

class Buttons:
    def __init__(self, parent):
        PX = 20
        PY = 20
        self.num_var = StringVar()
        self.num_var.set("0")

        self.b1 = Button(parent, text = "1", pady = PY, padx = PX)
        self.b1.grid(column = 1, row = 5, sticky = W)

        self.b2 = Button(parent, text = "2", pady = PY, padx = PX)
        self.b2.grid(column = 2, row = 5)

        self.b3 = Button(parent, text = "3", pady = PY, padx = PX)
        self.b3.grid(column = 3, row = 5)

        self.b4 = Button(parent, text = "4", pady = PY, padx = PX)
        self.b4.grid(column = 1, row = 4)
                
        self.b5 = Button(parent, text = "5", pady = PY, padx = PX)
        self.b5.grid(column = 2, row = 4)

        self.b6 = Button(parent, text = "6", pady = PY, padx = PX)
        self.b6.grid(column = 3, row = 4)
        
        self.b7 = Button(parent, text = "7", pady = PY, padx = PX)
        self.b7.grid(column = 1, row = 3)

        self.b8 = Button(parent, text = "8", pady = PY, padx = PX)
        self.b8.grid(column = 2, row = 3)

        self.b9 = Button(parent, text = "9", pady = PY, padx = PX)
        self.b9.grid(column = 3, row = 3)
        
        self.b0 = Button(parent, text = "0", pady = PY, padx = PX)
        self.b0.grid(column = 1, row = 6, columnspan = 2, sticky = E+W)

        self.bDecimal = Button(parent, text = ".", pady = PY, padx = PX)
        self.bDecimal.grid(column = 3, row = 6, sticky = W+E)

        self.bSubtraction = Button(parent, text = "-", pady = PY, padx = PX)
        self.bSubtraction.grid(column = 4, row = 6, sticky = W)

        self.bAddition = Button(parent, text = "+", pady = PY, padx = PX)
        self.bAddition.grid(column = 4, row = 5, sticky = W+E)

        self.bDivision = Button(parent, text = "/", pady = PY, padx = PX)
        self.bDivision.grid(column = 4, row = 4, sticky = W)

        self.bMultiplication = Button(parent, text = "*", pady = PY, padx = PX)
        self.bMultiplication.grid(column = 5, row = 4, sticky = W+E)

        self.bClear = Button(parent, text = "C", pady = PY, padx = PX)
        self.bClear.grid(column = 5, row = 1)

        self.bDelete = Button(parent, text = "CE", pady = PY, padx = PX)
        self.bDelete.grid(column = 4, row = 3, columnspan = 2, sticky = W+E)

        self.entryDisplay = Entry(parent)
        self.entryDisplay.grid(column = 1, row = 1, rowspan = 2, columnspan = 4, sticky = W+E+N+S)

        self.bEquals = Button(parent, text = "=", pady = PY, padx = PX)
        self.bEquals.grid(column = 5, row = 5, rowspan = 2, sticky = N+S+W+E)

if __name__ == "__main__":
    root = Tk()
    root.title("THS Calculator")
    calculator = Buttons(root)
    root.geometry("290x350+25+25")
    root.mainloop()
