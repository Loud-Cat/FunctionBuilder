from matplotlib import pyplot as plt
from math import *
from tkinter import *
from tkinter.font import Font

pad = lambda x=10,y=10: {"ipadx":x, "ipady":y}
class Window():
    def __init__(self):
        self.title_t = self.func_t = ""
        self.numbers = []
        self.bad = None
        
        self.xpi = [i * pi for i in range(-3, 4)]
        self.xlabels = [f'{i}$\pi$' for i in range(-3, 4)]
        self.xlabels[2:5] = '-$\pi$', '0', '$\pi$'
        self.x = [i / 100 for i in range(-942, 943)]

    def Plot(self):
        plt.xticks(self.xpi, self.xlabels)
        plt.xlim(-2.5*pi, 2.5*pi)
        plt.ylim(-3, 3)

        plt.gca().set_aspect('equal')
        plt.tight_layout(pad=2)
        plt.legend()
        plt.grid()
        plt.show()

    def Submit(self):
        self.title_t = self.title.get()
        self.func_t = self.func.get()
        try:
            plt.title(self.title_t)
            y = [eval(self.func_t) for x in self.x]
            self.numbers.append([y, self.func_t])
            self.bad = None
        except Exception as e:
            self.bad = e
            if self.func.get() == "":
                self.bad = "Please enter a function."
            
        for y,n in self.numbers:
            plt.plot(self.x,y, label=n)

        if not self.bad:
            self.Plot()
        self.root.destroy()
        self.main()

    def Clear(self):
        self.numbers = []
        self.title_t = self.func_t = ""
        self.title.delete(0, 'end')
        self.func.delete(0, 'end')

    def main(self):
        self.root = Tk()
        self.root.title("Custom Function Builder")
        self.box = Frame(self.root, width=300)
        self.box.grid(row=0, column=0, columnspan=2, **pad(10))

        self.info = Label(self.box, text="Custom Function Builder", font=Font(size=20))
        self.info.grid(row=0,column=0, columnspan=2, **pad(10))

        self.title_info = Label(self.box, text="Title:", font=Font(size=18))
        self.title_info.grid(row=1, column=0, **pad(10))

        self.title = Entry(self.box)
        self.title.insert(0, self.title_t)
        self.title.grid(row=1, column=1, **pad(10), pady=(0,10))

        self.func_info = Label(self.box, text="Function:", font=Font(size=18))
        self.func_info.grid(row=4, column=0, **pad(10))

        self.func = Entry(self.box)
        self.func.insert(0, self.func_t)
        self.func.grid(row=4, column=1, **pad(10), pady=(0,10))

        self.submit = Button(self.box, text="Submit!", font=Font(size=14), command=self.Submit)
        self.submit.grid(row=5, column=0, **pad(10))

        self.clear = Button(self.box, text="Clear the graph", font=Font(size=14), command=self.Clear)
        self.clear.grid(row=5, column=1, **pad(10))

        self.error = Label(self.box, text="Errors will appear here.")
        self.error.grid(row=6, column=0, columnspan=2, **pad(10))
        if self.bad:
            self.error.config(fg="red", text=f"Erorr! {self.bad}")
        
        self.box.grid(columnspan=2, ipadx=10, ipady=10)
        self.root.mainloop()

win = Window()
win.main()
