from cmath import sqrt
import math
import matplotlib.pyplot as plt
from numpy import append
import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import *

root= tk.Tk()
root.wm_title("Fully rational function")

canvas1 = tk.Canvas(root, width = 750, height = 500)
canvas1.pack()

entryA = tk.Entry (root) 
canvas1.create_window(130, 100, window=entryA, width = 40)

entryB = tk.Entry (root) 
canvas1.create_window(210, 100, window=entryB, width = 40)

entryC = tk.Entry (root) 
canvas1.create_window(290, 100, window=entryC, width = 40)

Solvertext = tk.Label(root, text='This is a solver for fully rational functions')
Solvertext.config(font=('helvetica', 14))
canvas1.create_window(238, 40, window=Solvertext)

Solverformat = tk.Label(root, text='The format is f(x)=ax²+bx+c')
Solverformat.config(font=('helvetica', 10))
canvas1.create_window(150, 60, window=Solverformat)

ValueA = tk.Label(root, text='a=')
ValueA.config(font=('helvetica', 10))
canvas1.create_window(100, 100, window=ValueA)

ValueB = tk.Label(root, text='b=')
ValueB.config(font=('helvetica', 10))
canvas1.create_window(180, 100, window=ValueB)

ValueC = tk.Label(root, text='c=')
ValueC.config(font=('helvetica', 10))
canvas1.create_window(260, 100, window=ValueC)

def FindFx():
    v1 = entryA.get()
    v2 = entryB.get()
    v3 = entryC.get()

    v1f2 = float(v1)**2

    if  v1.isnumeric()==False or v2.isnumeric()==False or v3.isnumeric()==False or float(v1) == 0:
        Valuefx = tk.Label(root, text="The Funktion is not fully rational",font=('helvetica', 10, 'bold'))
        canvas1.create_window(140, 140, window=Valuefx)

    elif float(v2) == 0:
        Valuefx = tk.Label(root, text="f(x)="+str(v1)+"x² +"+str(v3),font=('helvetica', 10, 'bold')) #fx
        canvas1.create_window(140, 140, window=Valuefx)

        Valuefx = tk.Label(root, text="f'(x)="+str(v1f2)+"x",font=('helvetica', 10, 'bold')) #f'x
        canvas1.create_window(140, 160, window=Valuefx)

        Valuefx = tk.Label(root, text="f''(x)="+str(v1f2),font=('helvetica', 10, 'bold')) #f''x
        canvas1.create_window(140, 180, window=Valuefx)

    else:
        Valuefx = tk.Label(root, text="f(x)="+str(v1)+"x² +"+str(v2)+"x +"+str(v3),font=('helvetica', 10, 'bold')) #fx
        Valuefx.place(x=140, y=140)

        Valuefx = tk.Label(root, text="f'(x)="+str(v1f2)+"x +"+str(v2),font=('helvetica', 10, 'bold')) #f'x
        Valuefx.place(x=140, y=160)

        Valuefx = tk.Label(root, text="f''(x)="+str(v1f2),font=('helvetica', 10, 'bold')) #f''x
        Valuefx.place(x=140, y=180)


buttonAdd = tk.Button(text='solve', command=FindFx, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 5)
canvas1.create_window(90, 190, window=buttonAdd)

root.mainloop()

#to do
#interface
#expand 
"""
print ("This is a solver for fully rational functions")
print ("The format is ax²+bx+c")

a = float (input ("please enter a value for a:")) #input
b = float (input ("please enter a value for b:"))
c = float (input ("please enter a value for c:"))
xt = float (input ("please enter the startpoint of the table:")) #table values
xe = float (input ("please enter the endpoint of the table:"))
s = float (input ("please enter the increment of the table:"))

a2 = float (2 * a)

if a == 0: #checking if fully rational

    print("The Funktion is not fully rational")

else:

    print ("The funktion f(x) is called: " + str(a) + "x² + " + str(b) + "x + " + str(c)) #f(x)
    print ("The funktion f(x)' is called: " + str(a2) + "x + " + str(b) )   #f'(x)
    print ("The funktion f(x)'' is: " + str(a2))   #f''(x)

    d = (b**2 - (4*a*c)) #discriminante

    if d > 0: #check discrimininante to find out the amount of x axis intersections

        x1 = float ((-b + (math.sqrt((b * b) - (4 * a * c)))) / (2 * a))
        x2 = float ((-b - (math.sqrt((b * b) - (4 * a * c)))) / (2 * a))
        
        print ("The funktion cuts the x axis at the points: x1= " + str(round(x1, 2)) + " und x2= " + str(round(x2, 2)))

    elif d == 0:

        x1 = float ((-b + (math.sqrt((b * b) - (4 * a * c)))) / (2 * a))

        print ("The funktion touches the x axis at the point: x1= " + str(round(x1, 2)))

    else:

        print ("The funktion does not touch the x axis.")
    
    Ex = float (- b / a2)
    Ey = float (a*Ex*Ex+b*Ex+c)

    if a > 0:   #checking if the function has a maximum or a minimum

        print ("There is a local minimum at the point: " + "(" + str(round(Ex, 2)) + "/" + str(round(Ey, 2)) + ")")

    else: 

        print ("There is a local maximum at the point: " + "(" + str(round(Ex, 2)) + "/" + str(round(Ey, 2)) + ")")

    xt = xt - s
    z = int(0) 

    print ("_____________________")
    print ("    X         Y    ")

    while xt < xe:  #drawing the table

        z = int(z + 1)
        xt = xt + s
        yt = a*xt*xt+b*xt+c
        print(" X" + str(z) + "= " + str(round(xt, 2)) + "    Y" + str(z) + "= " + str (round(yt, 2)))
        
    print ("_____________________")

    plt.rcParams["figure.figsize"] = [7.50, 3.50]   #drawing the graph/function
    plt.rcParams["figure.autolayout"] = True

def f(x):

   return a*x**2+b*x+c

x = np.linspace(-10, 10, 100)

plt.plot(x, f(x), color='red')

plt.show()
"""
