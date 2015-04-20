from tkinter import *

class Buttons:
    def __init__(self, parent):
        PX = 10
        PY = 10
        self.entryDisplay = StringVar()
        self.num_var = StringVar()
        self.num_var.set("0")

        self.b1 = Button(parent, text = "1", command = lambda: self.num_button(1), pady = PY, padx = PX)
        self.b1.grid(column = 1, row = 4, sticky = W)

        self.b2 = Button(parent, text = "2", command = lambda: self.num_button(2), pady = PY, padx = PX)
        self.b2.grid(column = 2, row = 4)

        self.b3 = Button(parent, text = "3", command = lambda: self.num_button(3),  pady = PY, padx = PX)
        self.b3.grid(column = 3, row = 4)

        self.b4 = Button(parent, text = "4", command = lambda: self.num_button(4),  pady = PY, padx = PX)
        self.b4.grid(column = 1, row = 3)
                
        self.b5 = Button(parent, text = "5", command = lambda: self.num_button(5),  pady = PY, padx = PX)
        self.b5.grid(column = 2, row = 3)

        self.b6 = Button(parent, text = "6", command = lambda: self.num_button(6),  pady = PY, padx = PX)
        self.b6.grid(column = 3, row = 3)
        
        self.b7 = Button(parent, text = "7", command = lambda: self.num_button(7),  pady = PY, padx = PX)
        self.b7.grid(column = 1, row = 2)

        self.b8 = Button(parent, text = "8", command = lambda: self.num_button(8),  pady = PY, padx = PX)
        self.b8.grid(column = 2, row = 2)

        self.b9 = Button(parent, text = "9", command = lambda: self.num_button(9),  pady = PY, padx = PX)
        self.b9.grid(column = 3, row = 2)
        
        self.b0 = Button(parent, text = "0", command = lambda: self.num_button(0),  pady = PY, padx = PX)
        self.b0.grid(column = 1, row = 5, columnspan = 2, sticky = E+W)

        self.bDecimal = Button(parent, text = ".", command = lambda: self.num_button("."),  pady = PY, padx = PX)
        self.bDecimal.grid(column = 3, row = 5, sticky = W+E)

        self.bSubtraction = Button(parent, text = "-", command = lambda: self.num_button("-"),  pady = PY, padx = PX)
        self.bSubtraction.grid(column = 4, row = 3, sticky = W+E)

        self.bAddition = Button(parent, text = "+", command = lambda: self.num_button("+"),  pady = PY, padx = PX)
        self.bAddition.grid(column = 5, row = 3, sticky = W+E)

        self.bDivision = Button(parent, text = "/", command = lambda: self.num_button("/"),  pady = PY, padx = PX)
        self.bDivision.grid(column = 4, row = 4, sticky = W+E)

        self.bMultiplication = Button(parent, text = "*", command = lambda: self.num_button("*"),  pady = PY, padx = PX)
        self.bMultiplication.grid(column = 5, row = 4, sticky = W+E)

        self.bClear = Button(parent, text = "clear", command = lambda: self.num_button("clear"),  pady = PY, padx = PX)
        self.bClear.grid(column = 4, row = 2)

        self.entryDisplay = Entry(parent)
        self.entryDisplay.grid(column = 1, row = 1, columnspan = 3, sticky = W+E)

        self.bEquals = Button(parent, text = "=", command = lambda: self.num_button("="),  pady = PY, padx = PX)
        self.bEquals.grid(column = 4, row = 5, columnspan = 2, sticky = W+E)

    def num_button(self, text):
        self.entryDisplay.insert(0, text)

if __name__ == "__main__":
    root = Tk()
    root.title = ("Simple Calculator")
    calculator = Buttons(root)
    root.geometry("200x200+25+25")
    root.iconbitmap("THS Logo.ico")
    root.mainloop()
