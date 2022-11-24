from tkinter import *

root = Tk()
root.title("Program collection")

root.geometry("720x550")

def tictactoe():
    import TicTacToe

def Fr_Funktion():
    import Fr_Funktion

def Calculator():
    import Calculator

def tictactoe_Ai():
    import TicTacToe_Ai
    
def Buttons_text():

    Description = Label(root, text='Program collection', font=(14)).place(anchor=CENTER, relx=.5, rely=.05)  # change to place if act up
    PlaceHolder = Button(root, text="               ", width=10, height=3, bd=0).grid(row=0, column=0)
    TicTacToe = Button(root, text="TicTacToe", width=10, height=5, command=tictactoe, bg='dark slate grey', fg='white').grid(row=1, column=1, padx=30, pady=25)
    TicTacToe_Ai = Button(root, text="TicTacToe Ai", width=10, command=tictactoe_Ai, height=5, bg='dark slate grey', fg='white').grid(row=1, column=2, padx=30, pady=25)
    Function = Button(root, text="Fr-Function", width=10, height=5, command=Fr_Funktion, bg='dark slate grey', fg='white').grid(row=1, column=3, padx=30, pady=25)
    calculator = Button(root, text="Calculator", width=10, height=5, command=Calculator, bg='dark slate grey', fg='white').grid(row=1, column=4, padx=30, pady=25)

Buttons_text()

root.mainloop()
