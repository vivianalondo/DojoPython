from tkinter import*

root = Tk()
root.geometry("1000x500+0+0")
root.title("Dojo UdeA (Python)")

#variable de control
text_Input = StringVar()
operator = ""


Tops = Frame(root, width = 1600,height = 80,bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

frame = Frame(root, width = 300,height = 700,bg="powder blue", relief=SUNKEN)
frame.pack(side=TOP)

lblInfo = Label(Tops, font=('SHOWCARD GOTHIC',50, 'bold'),text="Dojo Python UdeA \nDesarrollos Empresariales",fg="Steel Blue", bd=50)
lblInfo.grid(row=0,column=0)#Dibuja en la cuadrícula indicada

#=========================Calculator==============
def btnClick(numbres):
    global operator
    operator = operator + str(numbres)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup =str(eval(operator))
    text_Input.set(sumup)
    operator=""

def qExit():
    root.destroy()

txtDisplay = Entry(frame,font=('SHOWCARD GOTHIC',20, 'bold'), textvariable=text_Input, bd=30, 
                   bg="black", fg="white", justify='right')
txtDisplay.grid(columnspan=4)


# Los Numeros de la Calculadora
#=====================================================================================================================
btn7=Button(frame,padx=16, pady=10,bd=10, fg="black", font=('arial',20,'bold'),
            text="7", bg="powder blue", command=lambda:btnClick(7)).grid(row=2,column=0)

btn8=Button(frame,padx=16, pady=10,bd=10, fg="black", font=('arial',20,'bold'),
            text="8", bg="powder blue", command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(frame,padx=16, pady=10,bd=10, fg="black", font=('arial',20,'bold'),
            text="9", bg="powder blue", command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(frame,padx=16, pady=10,bd=10, fg="black", font=('arial',20,'bold'),
            text="+", bg="powder blue", command=lambda: btnClick("+")).grid(row=2,column=3)
#=====================================================================================================================
btn4=Button(frame,padx=16, pady=8,bd=8, fg="black", font=('arial',20,'bold'),
            text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(frame,padx=16, pady=8,bd=8, fg="black", font=('arial',20,'bold'),
            text="5", bg="powder blue", command=lambda: btnClick(5)).grid(row=3,column=1)

btn6=Button(frame,padx=16, pady=8,bd=8, fg="black", font=('arial',20,'bold'),
            text="6", bg="powder blue", command=lambda: btnClick(6)).grid(row=3,column=2)

Subtraction=Button(frame,padx=16, pady=10,bd=10, fg="black", font=('arial',20,'bold'),
            text="-", bg="powder blue", command=lambda: btnClick("-")).grid(row=3,column=3)
#=====================================================================================================================
btn1=Button(frame,padx=16, pady=8,bd=8, fg="black", font=('arial',20,'bold'),
            text="1", bg="powder blue", command=lambda: btnClick(1)).grid(row=4,column=0)

btn2=Button(frame,padx=16, pady=8,bd=8, fg="black", font=('arial',20,'bold'),
            text="2", bg="powder blue", command=lambda: btnClick(2)).grid(row=4,column=1)

btn3=Button(frame,padx=16, pady=8,bd=8, fg="black", font=('arial',20,'bold'),
            text="3", bg="powder blue", command=lambda: btnClick(3)).grid(row=4,column=2)

Multiply=Button(frame,padx=16, pady=10,bd=10, fg="black", font=('arial',20,'bold'),
            text="*", bg="powder blue", command=lambda: btnClick("*")).grid(row=4,column=3)
#=====================================================================================================================
btn0=Button(frame,padx=16, pady=8,bd=8, fg="black", font=('arial',20,'bold'),
            text="0", bg="powder blue", command=lambda: btnClick(0)).grid(row=5,column=0)

btnC=Button(frame,padx=16, pady=8,bd=8, fg="black", font=('arial',20,'bold'),
            text="C", bg="powder blue", command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(frame,padx=16, pady=8,bd=8, fg="black", font=('arial',20,'bold'),
            text="=", bg="powder blue", command=btnEqualsInput).grid(row=5,column=2)

Divide=Button(frame,padx=16, pady=10,bd=10, fg="black", font=('arial',20,'bold'),
            text="/", bg="powder blue", command=lambda: btnClick("/")).grid(row=5,column=3)
#=====================================================================================================================

root.mainloop()