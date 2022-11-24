from tkinter import *
from tkinter import messagebox
import random
import time

New = Tk()
New.title("TicTacToe")
New.geometry("450x450")
global count, x, Winner
x = True
count = 0
Winner = FALSE

def disable_all_buttons():

    S1.config(state=DISABLED)
    S2.config(state=DISABLED)
    S3.config(state=DISABLED)

    S4.config(state=DISABLED)
    S5.config(state=DISABLED)
    S6.config(state=DISABLED)

    S7.config(state=DISABLED)
    S8.config(state=DISABLED)   
    S9.config(state=DISABLED)

def Win():
    # X win
    global Winner

    if S1["text"] == "X" and S2["text"] == "X" and S3["text"] == "X":
        S1.config(bg="green")
        S2.config(bg="green")
        S3.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The player has won.")

    elif S4["text"] == "X" and S5["text"] == "X" and S6["text"] == "X":
        S4.config(bg="green")
        S5.config(bg="green")
        S6.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The player has won.")

    elif S7["text"] == "X" and S8["text"] == "X" and S9["text"] == "X":
        S7.config(bg="green")
        S8.config(bg="green")
        S9.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The player has won.")

    elif S1["text"] == "X" and S4["text"] == "X" and S7["text"] == "X":
        S1.config(bg="green")
        S4.config(bg="green")
        S7.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo("TicTacToe", "The player has won.")

    elif S2["text"] == "X" and S5["text"] == "X" and S8["text"] == "X":
        S2.config(bg="green")
        S5.config(bg="green")
        S8.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The player has won.")

    elif S3["text"] == "X" and S6["text"] == "X" and S9["text"] == "X":
        S3.config(bg="green")
        S6.config(bg="green")
        S9.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The player has won.")

    elif S1["text"] == "X" and S5["text"] == "X" and S9["text"] == "X":
        S1.config(bg="green")
        S5.config(bg="green")
        S9.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The player has won.")

    elif S3["text"] == "X" and S5["text"] == "X" and S7["text"] == "X":
        S3.config(bg="green")
        S5.config(bg="green")
        S7.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The player has won.")

    #Winner O

    elif S1["text"] == "O" and S2["text"] == "O" and S3["text"] == "O":
        S1.config(bg="green")
        S2.config(bg="green")
        S3.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The Ai has won.")

    elif S4["text"] == "O" and S5["text"] == "O" and S6["text"] == "O":
        S4.config(bg="green")
        S5.config(bg="green")
        S6.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The Ai has won.")

    elif S7["text"] == "O" and S8["text"] == "O" and S9["text"] == "O":
        S7.config(bg="green")
        S8.config(bg="green")
        S9.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The Ai has won.")

    elif S1["text"] == "O" and S4["text"] == "O" and S7["text"] == "O":
        S1.config(bg="green")
        S4.config(bg="green")
        S7.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The Ai has won.")

    elif S2["text"] == "O" and S5["text"] == "O" and S8["text"] == "O":
        S2.config(bg="green")
        S5.config(bg="green")
        S8.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The Ai has won.")

    elif S3["text"] == "O" and S6["text"] == "O" and S9["text"] == "O":
        S3.config(bg="green")
        S6.config(bg="green")
        S9.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The Ai has won.")

    elif S1["text"] == "O" and S5["text"] == "O" and S9["text"] == "O":
        S1.config(bg="green")
        S5.config(bg="green")
        S9.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The Ai has won.")

    elif S3["text"] == "O" and S5["text"] == "O" and S7["text"] == "O":
        S3.config(bg="green")
        S5.config(bg="green")
        S7.config(bg="green")
        Winner = TRUE
        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "The Ai has won.")

def AI():

    #Win Condition
    if S2["text"] == "O" and S3["text"] == "O" and S1["text"] != "X" or S4["text"] == "O" and S7["text"] == "O" and S1["text"] != "X" or S5["text"] == "O" and S9["text"] == "O" and S1["text"] != "X":
        S1["text"] = "O" 
        Win()

    elif S1["text"] == "O" and S3["text"] == "O" and S2["text"] != "X" or S5["text"] == "O" and S8["text"] == "O" and S2["text"] != "X":
        S2["text"] = "O"
        Win()    

    elif S1["text"] == "O" and S2["text"] == "O" and S3["text"] != "X" or S6["text"] == "O" and S9["text"] == "O" and S3["text"] != "X" or S5["text"] == "O" and S7["text"] == "O" and S3["text"] != "X":
        S3["text"] = "O"  
        Win()    

    elif S1["text"] == "O" and S7["text"] == "O" and S4["text"] != "X" or S5["text"] == "O" and S6["text"] == "O" and S4["text"] != "X":
        S4["text"] = "O"  
        Win()    

    elif S1["text"] == "O" and S9["text"] == "O" and S5["text"] != "X" or S2["text"] == "O" and S8["text"] == "O" and S5["text"] != "X" or S3["text"] == "O" and S7["text"] == "O" and S5["text"] != "X" or S4["text"] == "O" and S6["text"] == "O" and S5["text"] != "X":
        S5["text"] = "O" 
        Win()  

    elif S3["text"] == "O" and S9["text"] == "O" and S6["text"] != "X" or S5["text"] == "O" and S4["text"] == "O" and S6["text"] != "X":
        S6["text"] = "O" 
        Win()   

    elif S1["text"] == "O" and S4["text"] == "O" and S7["text"] != "X" or S8["text"] == "O" and S9["text"] == "O" and S7["text"] != "X":
        S7["text"] = "O"   
        Win() 

    elif S9["text"] == "O" and S7["text"] == "O" and S8["text"] != "X" or S5["text"] == "O" and S2["text"] == "O" and S8["text"] != "X":
        S8["text"] = "O"    
        Win() 

    elif S8["text"] == "O" and S7["text"] == "O" and S9["text"] != "X"  or S3["text"] == "O" and S6["text"] == "O" and S9["text"] != "X":
        S9["text"] = "O"     
        Win() 

    #Loss prevention
    elif S2["text"] == "X" and S3["text"] == "X" and S1["text"] != "O" and S1["text"] != "X" or S4["text"] == "X" and S7["text"] == "X" and S1["text"] != "O" and S1["text"] != "X" or S5["text"] == "X" and S9["text"] == "X" and S1["text"] != "O" and S1["text"] != "X":
        S1["text"] = "O" 
        Win()

    elif S1["text"] == "X" and S3["text"] == "X" and S2["text"] != "O" and S2["text"] != "X" or S5["text"] == "X" and S8["text"] == "X" and S2["text"] != "O" and S2["text"] != "X":
        S2["text"] = "O"
        Win()    

    elif S1["text"] == "X" and S2["text"] == "X" and S3["text"] != "O" and S3["text"] != "X" or S6["text"] == "X" and S9["text"] == "X" and S3["text"] != "O" and S3["text"] != "X" or S5["text"] == "X" and S7["text"] == "X" and S3["text"] != "O" and S3["text"] != "X":
        S3["text"] = "O"  
        Win()    

    elif S1["text"] == "X" and S7["text"] == "X" and S4["text"] != "O" and S4["text"] != "X" or S5["text"] == "X" and S6["text"] == "X" and S4["text"] != "O" and S4["text"] != "X":
        S4["text"] = "O"  
        Win()    

    elif S1["text"] == "X" and S9["text"] == "X" and S5["text"] != "O" and S5["text"] != "X" or S2["text"] == "X" and S8["text"] == "X" and S5["text"] != "O" and S5["text"] != "X" or S3["text"] == "X" and S7["text"] == "X" and S5["text"] != "O" and S5["text"] != "X" or S4["text"] == "X" and S6["text"] == "X" and S5["text"] != "O" and S5["text"] != "X":
        S5["text"] = "O" 
        Win()  

    elif S3["text"] == "X" and S9["text"] == "X" and S6["text"] != "O" and S6["text"] != "X" or S5["text"] == "X" and S4["text"] == "X" and S6["text"] != "O" and S6["text"] != "X":
        S6["text"] = "O" 
        Win()   

    elif S1["text"] == "X" and S4["text"] == "X" and S7["text"] != "O" and S7["text"] != "X" or S8["text"] == "X" and S9["text"] == "X" and S7["text"] != "O" and S7["text"] != "X":
        S7["text"] = "O"   
        Win() 

    elif S9["text"] == "X" and S7["text"] == "X" and S8["text"] != "O" and S8["text"] != "X" or S5["text"] == "X" and S2["text"] == "X" and S8["text"] != "O" and S8["text"] != "X":
        S8["text"] = "O"    
        Win() 

    elif S8["text"] == "X" and S7["text"] == "X" and S9["text"] != "O" and S9["text"] != "X"  or S3["text"] == "X" and S6["text"] == "X" and S9["text"] != "O" and S9["text"] != "X":
        S9["text"] = "O"     
        Win() 

    else:
        def Fallback():
            Random()
            if Ais["text"] == "O" or Ais["text"] == "X":
                Fallback()
            else:
                Ais["text"] = "O"
                Win()
        Fallback()

def Random():
    global Ais
    list1 = [S1,S2,S3,S4,S5,S6,S7,S8,S9]
    Ais = random.choice(list1)

def buttonclick(s):
    global count, Winner
    if count <= 3:

        if s["text"] == " " :
            s["text"] = "X"
            count += 1
            Win()

            if Winner == False:
                time.sleep(0.06)
                AI()    
    
    elif Winner == False:
        s["text"] = "X"
        Win()

        S1.config(bg="Red")
        S2.config(bg="Red")
        S3.config(bg="Red")

        S4.config(bg="Red")
        S5.config(bg="Red")
        S6.config(bg="Red")

        S7.config(bg="Red")
        S8.config(bg="Red")
        S9.config(bg="Red")

        disable_all_buttons()
        messagebox.showinfo(  "TicTacToe", "Draw.")

def Restart():

    global count, Winner

    count = 0
    Winner = False

    S1.config(state=NORMAL, bg="dark slate grey", text=" ")
    S2.config(state=NORMAL, bg="dark slate grey", text=" ")
    S3.config(state=NORMAL, bg="dark slate grey", text=" ")

    S4.config(state=NORMAL, bg="dark slate grey", text=" ")
    S5.config(state=NORMAL, bg="dark slate grey", text=" ")
    S6.config(state=NORMAL, bg="dark slate grey", text=" ")

    S7.config(state=NORMAL, bg="dark slate grey", text=" ")
    S8.config(state=NORMAL, bg="dark slate grey", text=" ")   
    S9.config(state=NORMAL, bg="dark slate grey", text=" ")

def TicTacButton():
    global S1, S2, S3, S4, S5, S6, S7, S8, S9
    Label(New, text='TicTacToe', font=('helvetica', 14)).place(x=172, y=14) #change
    Label(New, text="               ", width=10, height=3, bd=0).grid(row=0, column=0)
    Button(New, text="Reset", width=25, height=2, bg="Green", fg="white", command=Restart).place(x=133, y=380)

    S1 = Button(New, text=" ", width=10, height=5, fg='white', bg='dark slate grey', disabledforeground="white", command=lambda: buttonclick(S1))
    S2 = Button(New, text=" ", width=10, height=5, fg='white', bg='dark slate grey', disabledforeground="white", command=lambda: buttonclick(S2))
    S3 = Button(New, text=" ", width=10, height=5, fg='white', bg='dark slate grey', disabledforeground="white", command=lambda: buttonclick(S3))

    S4 = Button(New, text=" ", width=10, height=5, fg='white', bg='dark slate grey', disabledforeground="white", command=lambda: buttonclick(S4))
    S5 = Button(New, text=" ", width=10, height=5, fg='white', bg='dark slate grey', disabledforeground="white", command=lambda: buttonclick(S5))
    S6 = Button(New, text=" ", width=10, height=5, fg='white', bg='dark slate grey', disabledforeground="white", command=lambda: buttonclick(S6))

    S7 = Button(New, text=" ", width=10, height=5, fg='white', bg='dark slate grey', disabledforeground="white", command=lambda: buttonclick(S7))
    S8 = Button(New, text=" ", width=10, height=5, fg='white', bg='dark slate grey', disabledforeground="white", command=lambda: buttonclick(S8))
    S9 = Button(New, text=" ", width=10, height=5, fg='white', bg='dark slate grey', disabledforeground="white", command=lambda: buttonclick(S9))


    S1.grid(row=1, column=1, padx=10, pady=10)
    S2.grid(row=1, column=2, padx=10, pady=10)
    S3.grid(row=1, column=3, padx=10, pady=10)

    S4.grid(row=2, column=1, padx=10, pady=10)
    S5.grid(row=2, column=2, padx=10, pady=10)
    S6.grid(row=2, column=3, padx=10, pady=10)

    S7.grid(row=3, column=1, padx=10, pady=10)
    S8.grid(row=3, column=2, padx=10, pady=10)
    S9.grid(row=3, column=3, padx=10, pady=10)

TicTacButton()

New.mainloop()