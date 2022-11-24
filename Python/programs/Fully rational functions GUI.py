import math #imports
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import *
import os

#to do
#delete labels
#expand
#potentially clean up code

root= tk.Tk()
root.wm_title("Fully rational function")

root.geometry("750x580")

entryA = tk.Entry (root) 
entryA.place(x=130, y=100, width = 40)
entryB = tk.Entry (root) 
entryB.place(x=210, y=100, width = 40)
entryC = tk.Entry (root) 
entryC.place(x=290, y=100, width=40)
entryTs = tk.Entry (root) 
entryTs.place(x=520, y=100, width=40)
entryTe = tk.Entry (root) 
entryTe.place(x=600, y=100, width=40)
entryS = tk.Entry (root) 
entryS.place(x=680, y=100, width=40)


def Text_print(root):
    Solvertext = tk.Label(root, text='This is a solver for fully rational functions', font=('helvetica', 14))
    Solvertext.place(x=100, y=20)
    Solverformat = tk.Label(root, text='The format is f(x)=ax²+bx+c  (please dont leave any empty spaces)', font=('helvetica', 10))
    Solverformat.place(x=100, y=60)
    Derivatives = tk.Label(root, text='Derivatives of f(x):', font=('helvetica', 10, 'bold'))
    Derivatives.place(x=100, y=130)
    NST = tk.Label(root, text='y=0 values of f(x):', font=('helvetica', 10, 'bold'))
    NST.place(x=100, y=220)
    Extrema = tk.Label(root, text='Local extrema:', font=('helvetica', 10, 'bold'))
    Extrema.place(x=100, y=260)
    ValueA = tk.Label(root, text='a=', font=('helvetica', 10))
    ValueA.place(x=100, y=100)
    ValueB = tk.Label(root, text='b=', font=('helvetica', 10))
    ValueB.place(x=180, y=100)
    ValueC = tk.Label(root, text='c=', font=('helvetica', 10))
    ValueC.place(x=260, y=100)
    ValueTs = tk.Label(root, text='Ts=', font=('helvetica', 10))
    ValueTs.place(x=490, y=100)
    ValueTe = tk.Label(root, text='Te=', font=('helvetica', 10))
    ValueTe.place(x=570, y=100)
    ValueS = tk.Label(root, text='S=', font=('helvetica', 10))
    ValueS.place(x=658, y=100)
    TableX = tk.Label(root, text="X",font=('helvetica', 10)) 
    TableX.place(x=560, y=130)
    TableY = tk.Label(root, text="Y",font=('helvetica', 10)) 
    TableY.place(x=645, y=130)
    LegendTs = tk.Label(root, text="Ts= starting value of the table",font=('helvetica', 10)) 
    LegendTs.place(x=20, y=500)
    LegendTe = tk.Label(root, text="Te= end value of the table",font=('helvetica', 10)) 
    LegendTe.place(x=20, y=520)
    LegendS = tk.Label(root, text="S= increment of the table",font=('helvetica', 10)) 
    LegendS.place(x=20, y=540)

Text_print(root)

def FindFx(): #main solving command
    a = entryA.get()
    b = entryB.get()
    c = entryC.get()

    if  isReal(a)==False or isReal(b)==False or isReal(c)==False or float(a) == 0:

        Error = tk.Label(root, text="The Funktion is not fully rational",font=('helvetica', 10))
        Error.place(x=100, y=150)

        Clear = tk.Label(root, text="                                                                                                                                ")
        Clear.place(x=100, y=170) 
        Clear = tk.Label(root, text="                                                                                                                                ")
        Clear.place(x=100, y=190)
        Clear = tk.Label(root, text="                                                                                                                                ")
        Clear.place(x=100, y=240)
        Clear = tk.Label(root, text="                                                                                                                                ")
        Clear.place(x=100, y=280)
        return

    elif float(b) == 0:

            Clear = tk.Label(root, text="                                                                 ")
            Clear.place(x=100, y=150)          

            af2 = float(a)**2

            Valuefx = tk.Label(root, text="f(x)="+str(a)+"x² +"+str(c),font=('helvetica', 10)) #fx
            Valuefx.place(x=100, y=150)

            Valuefx2 = tk.Label(root, text="f'(x)="+str(af2)+"x",font=('helvetica', 10)) #f'x
            Valuefx2.place(x=100, y=170)

            Valuefx3 = tk.Label(root, text="f''(x)="+str(af2),font=('helvetica', 10)) #f''x
            Valuefx3.place(x=100, y=190)

    else:

            Clear = tk.Label(root, text="                                                                 ")
            Clear.place(x=100, y=150)

            af2 = float(a)**2

            Valuefx = tk.Label(root, text="f(x)="+str(a)+"x² +"+str(b)+"x +"+str(c),font=('helvetica', 10)) #fx
            Valuefx.place(x=100, y=150)

            Valuefx2 = tk.Label(root, text="f'(x)="+str(af2)+"x +"+str(b),font=('helvetica', 10)) #f'x
            Valuefx2.place(x=100, y=170)

            Valuefx3 = tk.Label(root, text="f''(x)="+str(af2),font=('helvetica', 10)) #f''x
            Valuefx3.place(x=100, y=190)

    d= float(b)**2 - (4*float(a)*float(c))

    if d > 0: #check discrimininante to find out the amount of x axis intersections

        x1 = (-float(b) + (math.sqrt((float(b)**2) - (4 * float(a) * float(c))))) / (2 * float(a))
        x2 = (-float (b) - (math.sqrt((float(b)**2) - (4 * float(a) * float(c))))) / (2 * float(a))

        nst = tk.Label(root, text="The funktion cuts the x axis at the points: x1= " + str(round(x1, 2)) + " und x2= " + str(round(x2, 2)),font=('helvetica', 10))
        nst.place(x=100, y=240)



    elif d == 0:

        x1 = (-float(b) + (math.sqrt((float(b)**2) - (4 * float(a) * float(c))))) / (2 * float(a))

        clear = tk.Label(root, text= "                                                                                   ")
        clear.place(x=100, y=240)
        nst = tk.Label(root, text="The funktion touches the x axis at the point: x1= " + str(round(x1, 2)),font=('helvetica', 10)) 
        nst.place(x=100, y=240)


    
    else:

        clear = tk.Label(root, text= "                                                                                   ")
        clear.place(x=100, y=240)
        nst = tk.Label(root, text="The funktion does not touch the x axis.",font=('helvetica', 10)) 
        nst.place(x=100, y=240)    

    Ex = - float(b) / float(af2)
    Ey = float(a)*float(Ex)*float(Ex)+float(b)*float(Ex)+float(c)

    if float(a) > 0:   #checking if the function has a maximum or a minimum

        Min = tk.Label(root, text="                                                           ")
        Min.config(text="There is a local minimum at the point: " + "(" + str(round(Ex, 2)) + "/" + str(round(Ey, 2)) + ")",font=('helvetica', 10)) 
        Min.place(x=100, y=280)

    else: 

        Max = tk.Label(root, text= "                                                          ") 
        Max.config(text="There is a local maximum at the point: " + "(" + str(round(Ex, 2)) + "/" + str(round(Ey, 2)) + ")",font=('helvetica', 10))
        Max.place(x=100, y=280)

def table(): #create table command

    Ts = entryTs.get()
    Te = entryTe.get()
    S = entryS.get()
    a = entryA.get()
    b = entryB.get()
    c = entryC.get()

    Z = int(0)
    Cx = float(130)

    Error = tk.Label(root, text="                                                                                     ") 
    Error.place(x=480, y=150)
    Error2 = tk.Label(root, text="                                                                                    ",) 
    Error2.place(x=480, y=170)

    if isReal(Ts)==False or isReal(Te)==False or isReal(S)==False or isReal(a)==False or isReal(b)==False or isReal(c)==False or float(Te)<=float(Ts):

        Error.config(text= "There was a problem processing your input.", font=('helvetica', 10))

        Error2.config(text="Please check your input again.",font=('helvetica', 10))

    else:

        Xt = float(Ts)-float(S)
        Te = float(Te)
        S = float(S)
        Ts = float(Ts)
        a = float(a)
        b = float(b)
        c = float(c)

        while Xt<Te:

            Z = Z+1
            Xt = Xt + S
            Yt = a*Xt*Xt+b*Xt+c
            Cx = Cx + 20

            Table = tk.Label(root, text="X" + str(Z) + "= " + str(round(Xt, 2)),font=('helvetica', 10)) 
            Table.place(x=540, y=Cx)
            Table = tk.Label(root, text="Y" + str(Z) + "= " + str(round(Yt, 2)),font=('helvetica', 10)) 
            Table.place(x=630, y=Cx)

def Graph(): #create graph command
    a = entryA.get()
    b = entryB.get()
    c = entryC.get()

    a = float(a)
    b = float(b)
    c = float(c)

    x = np.linspace(-5,5,100)

    y=a*x**2+b*x+c

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x,y, 'r')

    # show the plot
    plt.show()

def restart(): #restart button command
    root.destroy()
    os.startfile("Fully rational functions GUI.py")

def isReal(txt): #check if string is number
    try:
        float(txt)
        return True
    except ValueError:
        return False

def new_function(FindFx, table, Graph, restart):
    buttonAdd = tk.Button(text='Solve function', command=FindFx, bg='green', fg='white', font=('helvetica', 10, 'bold'), width = 15)
    buttonAdd.place(x=100, y=400)
    buttonAdd = tk.Button(text='Draw Graph F(x)', command=Graph, bg='green', fg='white', font=('helvetica', 10, 'bold'), width = 15)
    buttonAdd.place(x=250, y=400)
    buttonAdd = tk.Button(text='Restart Program', command=restart, bg='grey', fg='white', font=('helvetica', 10, 'bold'), width = 15)
    buttonAdd.place(x=595, y=20)
    buttonAddtable = tk.Button(text='Fill Table', command= table, bg='green', fg='white', font=('helvetica', 10, 'bold'), width = 15)
    buttonAddtable.place(x=250, y=440)

new_function(FindFx, table, Graph, restart)

root.mainloop()
