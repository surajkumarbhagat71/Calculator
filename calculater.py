from tkinter import *

expression = ""

def clear():
    global expression
    expression = ""
    displayValue.set(expression)


def equal():
    global expression
    expression = str(eval(expression))
    displayValue.set(expression)

def btnClick(num):
    global expression
    expression += str(num)
    displayValue.set(expression)
    
    


win = Tk()
win.title("cws Calculator")
win.geometry("462x300")
win.configure(background="light green")

displayValue = StringVar()

displayValue.set("lets Calculate")


display = Entry(win,width=70,justify=RIGHT,textvariable=displayValue ) 

display.grid(row=0,columnspan=4 , pady = 20,padx = 10)


#----------------------------------- 1st Row -------------------------------#

btn1 = Button(win,width=10,height=2,fg = "black",bg="white",text="1" ,command=lambda:btnClick(1))

btn1.grid(row=1,column=0)

btn1 = Button(win,width=10,height=2,fg = "black",bg="white",text="2" , command=lambda:btnClick(2))

btn1.grid(row=1,column=1)

btn1 = Button(win,width=10,height=2,fg = "black",bg="white",text="3",command=lambda:btnClick(3))

btn1.grid(row=1,column=2)

btn1 = Button(win,width=10,height=2,fg = "black",bg="white",text="+", command =lambda:btnClick('+'))

btn1.grid(row=1,column=3)

#-------------------------------  2nd row ---------------------#

btn2 = Button(win,width=10,height=2,fg = "black",bg="white",text="4",command=lambda:btnClick(4))

btn2.grid(row=2,column=0)

btn2 = Button(win,width=10,height=2,fg = "black",bg="white",text="5" ,command=lambda:btnClick(5))

btn2.grid(row=2,column=1)

btn2 = Button(win,width=10,height=2,fg = "black",bg="white",text="6",command=lambda:btnClick(6))

btn2.grid(row=2,column=2)

btn2 = Button(win,width=10,height=2,fg = "black",bg="white",text="/",command=lambda:btnClick('/'))

btn2.grid(row=2,column=3)


#----------------------- 3rd Row --------------


btn3 = Button(win,width=10,height=2,fg = "black",bg="white",text="7",command=lambda:btnClick(7))

btn3.grid(row=3,column=0)

btn3 = Button(win,width=10,height=2,fg = "black",bg="white",text="7",command=lambda:btnClick(8))

btn3.grid(row=3,column=1)

btn3 = Button(win,width=10,height=2,fg = "black",bg="white",text="9",command=lambda:btnClick(9))

btn3.grid(row=3,column=2)

btn3 = Button(win,width=10,height=2,fg = "black",bg="white",text="*",command=lambda:btnClick("*"))

btn3.grid(row=3,column=3)


#----------------------- 4th row-----------------------

btn4 = Button(win,width=10,height=2,fg = "black",bg="white",text="0",command=lambda:btnClick(0))

btn4.grid(row=4,column=0)

btn4 = Button(win,width=10,height=2,fg = "black",bg="white",text="=" ,command = equal)

btn4.grid(row=4,column=1)

btn4 = Button(win,width=10,height=2,fg = "white",bg="red",text="c", command = clear )

btn4.grid(row=4,column=2)

btn4 = Button(win,width=10,height=2,fg = "black",bg="white",text="-")

btn4.grid(row=4,column=3)


win.mainloop()
