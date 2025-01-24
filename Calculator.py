'''
project name    : Calculator
designed by     : Dinesh Kumar G
designed on     : 23.01.2025 , 10:27pm
purpose         :Creating a GUI based Calculator
'''
from tkinter import * #importing the tkinter package for GUI based model

#assign the tkinter package into the variable cal
cal=Tk() 

#Title of the GUI based model
cal.title("Calculator") 

#Giving the Geometry(height,width)
cal.geometry('250x350')

#Creating a Message Box for Collecting Inputs from User
equation=StringVar()
entry=Entry(cal,textvariable=equation,font=('aerial',15))
entry.grid(row=0,column=0,columnspan=4)

#Creating a Function to Calulate the Value given by the user
def update(value):
    current_value=equation.get()
    equation.set(current_value + value)

#Clearing the Screen or Message Box for Further Calculation
def clear():
    equation.set(" ")


#For Calulate the values given by the User
def calculation():
    try:
        result=eval(equation.get())
        equation.set(result)
    except Exception as e:
        equation.set("Error")

#created the buttons that can be used by the user
button=[
    'C','% ','000','/',
    '9','8','7','*',
    '6','5','4','-',
    '3','2','1','+',
    '00','0','.','='
]
r=1 #row
c=0 #column
for b in button:
    if b == 'C':
        button_1=Button(cal,text=b,pady=20,padx=20,command=clear)
    elif b == '=':
        button_1=Button(cal,text=b,pady=20,padx=20,command=calculation)
    else:
        button_1=Button(cal,text=b,pady=20,padx=20,command=lambda button=b:update(button))
    button_1.grid(row=r,column=c)
    c = c + 1
    if c > 3:
        c=0
        r = r +1




#Calling the cal variable to execute the GUI based model
cal.mainloop()