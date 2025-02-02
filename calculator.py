from tkinter import Tk, Entry, Button, StringVar


class Calculator:
    def __init__(self, master):
        width = 357
        height = 470
        master.title("Simple Calculator by HaniffZaid")
        master.geometry(f'{width}x{height}+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.result = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#aabbcc', foreground='black', font=('Arial Bold', 40), textvariable=self.equation).place(x=0, y=0)
        Entry(width=17, bg='#aabbcc', foreground='darkblue', font=('Arial Bold', 28), textvariable=self.result).place(x=0, y=50)
        Button(width=11, height=4, text='(', relief='flat', bg='lightpink', command=lambda: self.show('(')).place(x=0, y=100)
        Button(width=11, height=4, text=')', relief='flat', bg='lightpink', command=lambda: self.show(')')).place(x=90, y=100)
        Button(width=11, height=4, text='%', relief='flat', bg='lightpink', command=lambda: self.show('%')).place(x=180, y=100)
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show(1)).place(x=0, y=175)
        Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show(2)).place(x=90, y=175)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show(3)).place(x=180, y=175)
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show(4)).place(x=0, y=250)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show(5)).place(x=90, y=250)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show(6)).place(x=180, y=250)
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show(7)).place(x=0, y=325)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show(8)).place(x=180, y=325)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show(9)).place(x=90, y=325)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show(0)).place(x=90, y=400)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=180, y=400)
        Button(width=11, height=4, text='+', relief='flat', bg='lightpink', command=lambda: self.show('+')).place(x=270, y=325)
        Button(width=11, height=4, text='-', relief='flat', bg='lightpink', command=lambda: self.show('-')).place(x=270, y=250)
        Button(width=11, height=4, text='/', relief='flat', bg='lightpink', command=lambda: self.show('/')).place(x=270, y=100)
        Button(width=11, height=4, text='x', relief='flat', bg='lightpink', command=lambda: self.show('*')).place(x=270, y=175)
        Button(width=11, height=4, text='=', relief='flat', bg='lightpink', command=self.solve).place(x=270, y=400)
        Button(width=11, height=4, text='C', relief='flat', bg='maroon', command=self.clear).place(x=0, y=400)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)
        self.result.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.result.set(f"Result:  {result}")


if __name__ == '__main__':
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()