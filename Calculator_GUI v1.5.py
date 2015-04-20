# GUI Only
#Jack Hay 2/04/15
from tkinter import *

class Buttons:
    def __init__(self, parent):
        display = StringVar()
        PX = 20
        PY = 20
        self.num_var = StringVar()
        self.num_var.set("0")

        self.b1 = Button(parent, text = "1", command = self.Disp1, pady = PY, padx = PX)
        self.b1.grid(column = 1, row = 5, sticky = W)

        self.b2 = Button(parent, text = "2", command = self.Disp2, pady = PY, padx = PX)
        self.b2.grid(column = 2, row = 5)

        self.b3 = Button(parent, text = "3", command = self.Disp3, pady = PY, padx = PX)
        self.b3.grid(column = 3, row = 5)

        self.b4 = Button(parent, text = "4", command = self.Disp4, pady = PY, padx = PX)
        self.b4.grid(column = 1, row = 4)
                
        self.b5 = Button(parent, text = "5", command = self.Disp5, pady = PY, padx = PX)
        self.b5.grid(column = 2, row = 4)

        self.b6 = Button(parent, text = "6", command = self.Disp6, pady = PY, padx = PX)
        self.b6.grid(column = 3, row = 4)
        
        self.b7 = Button(parent, text = "7", command = self.Disp7, pady = PY, padx = PX)
        self.b7.grid(column = 1, row = 3)

        self.b8 = Button(parent, text = "8", command = self.Disp8, pady = PY, padx = PX)
        self.b8.grid(column = 2, row = 3)

        self.b9 = Button(parent, text = "9", command = self.Disp9, pady = PY, padx = PX)
        self.b9.grid(column = 3, row = 3)
        
        self.b0 = Button(parent, text = "0", command = self.Disp0, pady = PY, padx = PX)
        self.b0.grid(column = 1, row = 6, columnspan = 2, sticky = E+W)

        self.bDecimal = Button(parent, text = ".", command = self.DispDec, pady = PY, padx = PX)
        self.bDecimal.grid(column = 3, row = 6, sticky = W+E)

        self.bSubtraction = Button(parent, text = "-", command = self.DispSub, pady = PY, padx = PX)
        self.bSubtraction.grid(column = 4, row = 6, sticky = W)

        self.bAddition = Button(parent, text = "+", command = self.DispAdd, pady = PY, padx = PX)
        self.bAddition.grid(column = 4, row = 5, sticky = W+E)

        self.bDivision = Button(parent, text = "/", command = self.DispDiv, pady = PY, padx = PX)
        self.bDivision.grid(column = 4, row = 4, sticky = W)

        self.bMultiplication = Button(parent, text = "*", command = self.DispMult, pady = PY, padx = PX)
        self.bMultiplication.grid(column = 5, row = 4, sticky = W+E)

        self.bClear = Button(parent, text = "C", command = self.Clear, pady = PY, padx = PX)
        self.bClear.grid(column = 5, row = 1)

        self.bDelete = Button(parent, text = "CE", pady = PY, padx = PX)
        self.bDelete.grid(column = 4, row = 3, columnspan = 2, sticky = W+E)

        self.entryDisplay = Entry(parent, textvariable = display)
        self.entryDisplay.grid(column = 1, row = 1, rowspan = 2, columnspan = 4, sticky = W+E+N+S)

        self.bEquals = Button(parent, text = "=", pady = PY, padx = PX)
        self.bEquals.grid(column = 5, row = 5, rowspan = 2, sticky = N+S+W+E)

    def Disp1(self):
        self.entryDisplay.insert(0, "1")

    def Disp2(self):
        self.entryDisplay.insert(0, "2")

    def Disp3(self):
        self.entryDisplay.insert(0, "3")

    def Disp4(self):
        self.entryDisplay.insert(0, "4")

    def Disp5(self):
        self.entryDisplay.insert(0, "5")

    def Disp6(self):
        self.entryDisplay.insert(0, "6")

    def Disp7(self):
        self.entryDisplay.insert(0, "7")

    def Disp8(self):
        self.entryDisplay.insert(0, "8")

    def Disp9(self):
        self.entryDisplay.insert(0, "9")

    def Disp0(self):
        self.entryDisplay.insert(0, "0")

    def DispAdd(self):
        self.entryDisplay.insert(0, "+")

    def DispSub(self):
        self.entryDisplay.insert(0, "-")

    def DispDiv(self):
        self.entryDisplay.insert(0, "/")

    def DispMult(self):
        self.entryDisplay.insert(0, "*")

    def DispDec(self):
        self.entryDisplay.insert(0, ".")

    def Clear(self):
        self.entryDisplay.delete(0, END)
if __name__ == "__main__":
    root = Tk()
    root.title("THS Calculator")
    calculator = Buttons(root)
    root.geometry("290x350+25+25")
    root.mainloop()
