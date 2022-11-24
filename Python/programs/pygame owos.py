from tkinter import *

root = Tk()
root.title("Program collection")

root.geometry("720x550")

def tictactoe():
    from TicTacToe import TicTacButton
    TicTacButton()

def Buttons_text(root):

    Description = Label(root, text='Program collection', font=(14)).place(anchor=CENTER, relx=.5, rely=.05)  # change to place if act up
    PlaceHolder = Button(root, text="               ", width=10, height=3, bd=0).grid(row=0, column=0)
    TicTacToe = Button(root, text="TicTacToe", width=10, height=5, command=tictactoe, bg='dark slate grey', fg='white').grid(row=1, column=1, padx=30, pady=25)
    Placeholder1 = Button(root, text="PLaceholder", width=10, height=5, bg='dark slate grey', fg='white').grid(row=1, column=2, padx=30, pady=25)
    PLaceholder2 = Button(root, text="PLaceholder", width=10, height=5, bg='dark slate grey', fg='white').grid(row=1, column=3, padx=30, pady=25)
    PLaceholder3 = Button(root, text="PLaceholder", width=10, height=5, bg='dark slate grey', fg='white').grid(row=1, column=4, padx=30, pady=25)

Buttons_text(root)

root.mainloop()
