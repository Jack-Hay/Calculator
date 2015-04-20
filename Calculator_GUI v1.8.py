from tkinter import *

class Buttons:
    def __init__(self, parent):
        self.entryDisplay = StringVar()
        button_layout = ["7", "8", "9","C","CE", "4", "5", "6", "/", "*",
                         "1", "2", "3", "+", "-", "0", ".", "="]
        col = 0
        rows = 2
        PY = 20
        PX = 20

        self.entryScreen = Entry(parent, textvariable = self.entryDisplay)
        self.entryScreen.grid(column = 1, row = 1, columnspan = 3, sticky = W+E)
        
        for i in button_layout:
            self.Calculator_Buttons = Button(parent, text = i, command = lambda i=i: self.enterButton(i), pady = PY, padx = PX).grid(row = rows, column = col, sticky = N+E+W+S)
            col = col + 1
            if i == "=":
                Button(parent, text = i, command = lambda i=i: self.enterButton(i), padx = PX, pady = PY).grid(row = 5, column = 4, columnspan = 2)
            elif i == "0":
                Button(parent, text = i, command = lambda i=i: self.enterButton(i), padx = PX, pady = PY).grid(row = 5, column = 0, columnspan = 2, sticky = W + E)
            elif i == ".":
                Button(parent, text = i, command = lambda i=i: self.enterButton(i), padx = PX, pady = PY).grid(row = 5, column = 2)
            if col > 4:
                rows = rows +1
                col = 0

                
    def enterButton(self, i):
        if i == "C":
            self.entryScreen.delete(0, END)

        elif i == "+":
            operand1 = self.entryScreen.get()
            self.entryScreen.insert(0, i)

        elif i == "=":
            ans = eval(self.entryScreen.get())
            self.entryScreen.delete(0,END)
            self.entryScreen.insert(0,ans)

        else:
            self.entryScreen.insert(0, i)




if __name__ == "__main__":
    root = Tk()
    calculator = Buttons(root)
    root.geometry("400x400+25+25")
    root.mainloop()
