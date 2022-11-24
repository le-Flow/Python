from cmath import sqrt
import math
import matplotlib.pyplot as plt
from numpy import append
import numpy as np
from matplotlib import pyplot as plt

#to do
#interface
#expand 

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

