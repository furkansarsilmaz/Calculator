from tkinter import *
from tkinter import messagebox
class calculator:
    def __init__(self,root):
        self.root = root
        self.root.geometry("250x340")
        self.root.title("Calculator")
        self.root.configure(background="gray")
        self.operation = ""
        self.result = StringVar()

        self.equal_label = Label(self.root,textvariable=self.result,width=25,height=2)
        self.equal_label.pack(pady=10)

        self.button_frame = Frame(self.root,background="gray")
        self.button_frame.pack()

        self.button_1 = Button(self.button_frame,text="1",width=5,height=3,command=lambda:self.press_button(1))
        self.button_1.grid(row=2,column=0)
        
        self.button_2 = Button(self.button_frame,text="2",width=5,height=3,command=lambda:self.press_button(2))
        self.button_2.grid(row=2,column=1)

        self.button_3 = Button(self.button_frame,text="3",width=5,height=3,command=lambda:self.press_button(3))
        self.button_3.grid(row=2,column=2)

        self.button_4 = Button(self.button_frame,text="4",width=5,height=3,command=lambda:self.press_button(4))
        self.button_4.grid(row=1,column=0)

        self.button_5 = Button(self.button_frame,text="5",width=5,height=3,command=lambda:self.press_button(5))
        self.button_5.grid(row=1,column=1)

        self.button_6 = Button(self.button_frame,text="6",width=5,height=3,command=lambda:self.press_button(6))
        self.button_6.grid(row=1,column=2)

        self.button_7 = Button(self.button_frame,text="7",width=5,height=3,command=lambda:self.press_button(7))
        self.button_7.grid(row=0,column=0)

        self.button_8 = Button(self.button_frame,text="8",width=5,height=3,command=lambda:self.press_button(8))
        self.button_8.grid(row=0,column=1)

        self.button_9 = Button(self.button_frame,text="9",width=5,height=3,command=lambda:self.press_button(9))
        self.button_9.grid(row=0,column=2)

        self.button_divide = Button(self.button_frame,text="/",width=5,height=3,command=lambda:self.press_button("/"))
        self.button_divide.grid(row=0,column=3)

        self.button_times = Button(self.button_frame,text="*",width=5,height=3,command=lambda:self.press_button("*"))
        self.button_times.grid(row=1,column=3)

        self.button_minus = Button(self.button_frame,text="-",width=5,height=3,command=lambda:self.press_button("-"))
        self.button_minus.grid(row=2,column=3)

        self.button_plus = Button(self.button_frame,text="+",width=5,height=3,command=lambda:self.press_button("+"))
        self.button_plus.grid(row=3,column=3)

        self.button_clear = Button(self.button_frame,text="C",width=5,height=3,command=lambda:self.Clear())
        self.button_clear.grid(row=3,column=0)

        self.button_0 = Button(self.button_frame,text="0",width=5,height=3,command=lambda:self.press_button(0))
        self.button_0.grid(row=3,column=1)

        self.button_point = Button(self.button_frame,text=".",width=5,height=3,command=lambda:self.press_button("."))
        self.button_point.grid(row=3,column=2)

        self.button_equal = Button(self.button_frame,text="=",width=5,height=3,command=lambda:self.equal())
        self.button_equal.grid(row=4,column=0)

    def equal(self):
        try:
            total = str(eval(self.operation))
            self.result.set(total)
            self.operation = total
        except SyntaxError:
            messagebox.showerror("Error","Syntax Error !!")
            self.operation = ""
        except ZeroDivisionError:
            messagebox.showerror("Error","Zero Division Error !!")
            self.operation = ""

    def press_button(self,num):
        self.operation += str(num)
        self.result.set(self.operation)

    def Clear(self):
        self.operation = ""
        self.result.set("")

if __name__ == "__main__":
    root = Tk()
    calculator(root)
    root.mainloop()