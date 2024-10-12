from tkinter import *

def Press_Button(num):
    global Equation_text
    Equation_text += str(num)
    Equation_Label.set(Equation_text)

def Equal():
    global Equation_text
    try :
        Total = str(eval(Equation_text))
        Equation_Label.set(Total)
        Equation_text = Total
    except SyntaxError :
        Equation_Label.set("Syntax Error..")
        Equation_text = ""
    except ZeroDivisionError :
        Equation_Label.set("Arithmetic Error..")
        Equation_text = ""



def Clear():
    global Equation_text
    Equation_Label.set("")
    Equation_text = ""

Window = Tk()
Window.title("Calculator")
Window.geometry("500x500")
Window.configure(background="gray")

# Creating Operation Line
Equation_text = ""
Equation_Label = StringVar()

Label = Label(Window,
textvariable = Equation_Label,
font=("Arial",20),
bg="white",
width=24,
height=2
)
Label.pack(pady=10)

#Creating Frame for Buttons
Frame_Button = Frame(Window,bg = "gray",width = 100,height = 60)
Frame_Button.pack()

# First Row of The Numbers
Button7 = Button(Frame_Button,text = 7,height = 4,width = 9,command = lambda:Press_Button(7))
Button7.grid(row = 0,column = 0)

Button8 = Button(Frame_Button,text = 8,height = 4,width = 9,command = lambda: Press_Button(8))
Button8.grid(row = 0,column = 1)

Button9 = Button(Frame_Button,text = 9,height = 4,width = 9,command = lambda:Press_Button(9))
Button9.grid(row = 0,column = 2)

#Second Row of The Numbers
Button4 = Button(Frame_Button,height = 4,width = 9,text = 4,command = lambda:Press_Button(4))
Button4.grid(row = 1,column = 0)

Button5 = Button(Frame_Button,text = 5,width = 9,height = 4,command = lambda: Press_Button(5))
Button5.grid(row = 1,column = 1)

Button6 = Button(Frame_Button,text = 6,width = 9,height = 4,command = lambda:Press_Button(6))
Button6.grid(row = 1,column = 2)

#Third Row of the Numbers
Button1 = Button(Frame_Button,text = 1,width = 9,height = 4,command = lambda:Press_Button(1))
Button1.grid(row = 2,column= 0)

Button2 = Button(Frame_Button,text = 2,width = 9,height = 4,command = lambda:Press_Button(2)    )
Button2.grid(row =2,column = 1)

Button3 = Button(Frame_Button,text = 3,width = 9,height = 4,command = lambda:Press_Button(3))
Button3.grid(row = 2,column = 2)

Button_Clear = Button(Frame_Button,text = "Clear",height = 4,width = 9,command = lambda: Clear())
Button_Clear.grid(row =3,column=0)

#Operation Column
Button_Divide = Button(Frame_Button,text = "/",height = 4,width = 9,command= lambda:Press_Button("/"))
Button_Divide.grid(row = 0,column =3 )

Button_Times = Button(Frame_Button,text="*",height = 4,width = 9,command= lambda:Press_Button("*"))
Button_Times.grid(row =1,column =3)

Button_Minus = Button(Frame_Button,text = "-",height = 4,width = 9,command = lambda: Press_Button("-") )
Button_Minus.grid(row = 2,column = 3)

Button_Plus = Button(Frame_Button,text= "+" ,height= 4,width= 9,command = lambda: Press_Button("+"),)
Button_Plus.grid(row =3,column =3)

Button0 = Button(Frame_Button,text = 0,height= 4,width= 9,command = lambda: Press_Button(0))
Button0.grid(row =3,column =1)

Button_Point = Button(Frame_Button,text= ".",height= 4,width= 9,command = lambda: Press_Button("."))
Button_Point.grid(row =3,column=2)

Button_Equal = Button(Frame_Button,text = "=",height = 4,width = 9,command = lambda: Equal())
Button_Equal.grid(row = 4,column =0)

Window.mainloop()

