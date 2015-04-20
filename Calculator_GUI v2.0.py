from tkinter import *

class Buttons:
    def __init__(self, parent):
        self.entryDisplay = StringVar()
        number_layout = ["7", "8", "9", "4", "5", "6",
                         "1", "2", "3", "0", "."]
        col = 0
        rows = 2
        PY = 20
        PX = 20
        
        self.entryScreen = StringVar()
        self.entryScreen = Entry(parent, textvariable = self.entryDisplay)
        
        self.entryScreen.grid(column = 1, row = 1, columnspan = 3, sticky = W+E)

        operator_layout = ["*", "/", "-", "+", "="]
        col2 = 3
        rows2 = 2
        for i in number_layout:
            self.Calculator_Buttons = Button(parent, text = i, command = lambda i=i: self.enterButton(i), bg = "#add8e6", pady = PY, padx = PX).grid(row = rows, column = col, sticky = N+E+W+S)
            col = col + 1
                
            if col > 2:
                rows = rows +1
                col = 0

        for i in operator_layout:
            
            self.Calculator_Buttons = Button(parent, text = i, command = lambda i=i: self.enterButton(i), bg = "yellow", pady = PY, padx = PX).grid(row = rows, column = col, sticky = N+E+W+S)
            col2 = col2 + 1

            if col2 > 4:
                rows2 = rows2 + 1
                col2 = 3

                
    def enterButton(self, i):
        if i == "C":
            self.entryScreen.delete(0, END)

        elif i == "+":
            operand1 = self.entryScreen.get()
            self.entryScreen.insert(END, i)

        elif i == "=":
            ans = eval(self.entryScreen.get())
            self.entryScreen.delete(0, END)
            self.entryScreen.insert(0, ans)

        else:
            self.entryScreen.insert(END, i)
            




if __name__ == "__main__":
    root = Tk()
    calculator = Buttons(root)
    root.geometry("400x400+25+25")
    root.mainloop()
