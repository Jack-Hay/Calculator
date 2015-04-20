from tkinter import *

class Buttons:
    def __init__(self, parent):
        PX = 2
        PY = 2
        self.num_var = StringVar()
        self.num_var.set("0")

        self.button_frame = Frame(parent, width = 300, height = 320, bg = "grey")
        self.button_frame.grid_propagate(0)

        self.b1 = Button(self.button_frame, text = "1")
        self.b1.grid(column = 1, row = 4, sticky = W)

        self.b2 = Button(self.button_frame, text = "2")
        self.b2.grid(column = 2, row = 4)

        self.b3 = Button(self.button_frame, text = "3")
        self.b3.grid(column = 3, row = 4)

        self.b4 = Button(self.button_frame, text = "4")
        self.b4.grid(column = 1, row = 3)
                
        self.b5 = Button(self.button_frame, text = "5")
        self.b5.grid(column = 2, row = 3)

        self.b6 = Button(self.button_frame, text = "6")
        self.b6.grid(column = 3, row = 3)
        
        self.b7 = Button(self.button_frame, text = "7")
        self.b7.grid(column = 1, row = 2)

        self.b8 = Button(self.button_frame, text = "8")
        self.b8.grid(column = 2, row = 2)

        self.b9 = Button(self.button_frame, text = "9")
        self.b9.grid(column = 3, row = 2)
        
        self.b0 = Button(self.button_frame, text = "0")
        self.b0.grid(column = 1, row = 5, columnspan = 2)

if __name__ == "__main__":
    root = Tk()
    root.title = ("Simple Calculator")
    calculator = Buttons(root)
    root.geometry("400x400+25+25")
    root.mainloop()
