from tkinter import *

NewCalc= Tk()

canvas1 = Canvas(NewCalc, width = 300, height = 300)
canvas1.pack()

entry1 = Entry (NewCalc) 
canvas1.create_window(210, 100, window=entry1)

entry2 = Entry (NewCalc) 
canvas1.create_window(210, 140, window=entry2)

entry3 = Entry (NewCalc) 
canvas1.create_window(210, 240, window=entry3)

label0 = Label(NewCalc, text='Calculator')
label0.config(font=('helvetica', 14))
canvas1.create_window(150, 40, window=label0)

label1 = Label(NewCalc, text='Type Value 1:')
label1.config(font=('helvetica', 10))
canvas1.create_window(100, 100, window=label1)

label2 = Label(NewCalc, text='Type Value 2:')
label2.config(font=('helvetica', 10))
canvas1.create_window(100, 140, window=label2)

label3 = Label(NewCalc, text='Result:')
label3.config(font=('helvetica', 10))
canvas1.create_window(100, 240, window=label3)

def add():  
    v1 = entry1.get()
    v2 = entry2.get()
  
    label4 = Label(NewCalc, text= float(v1)+float(v2),font=('helvetica', 10, 'bold'),bg='white')
    canvas1.create_window(210, 240, window=label4)
      
buttonAdd = Button(NewCalc, text='+', command=add, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 5)
canvas1.create_window(90, 190, window=buttonAdd)

def sub():  
    v1 = entry1.get()
    v2 = entry2.get()
  
    label5 = Label(NewCalc, text= float(v1)-float(v2),font=('helvetica', 10, 'bold'),bg='white')
    canvas1.create_window(210, 240, window=label5)
      
buttonSub = Button(NewCalc, text='–', command=sub, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 5)
canvas1.create_window(140, 190, window=buttonSub)

def mul():  
    v1 = entry1.get()
    v2 = entry2.get()
  
    label6 = Label(NewCalc, text= float(v1)*float(v2),font=('helvetica', 10, 'bold'),bg='white')
    canvas1.create_window(210, 240, window=label6)
      
buttonMul = Button(NewCalc, text='x', command=mul, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 5)
canvas1.create_window(190, 190, window=buttonMul)

def div():  
    v1 = entry1.get()
    v2 = entry2.get()
  
    label7 = Label(NewCalc, text= float(v1)/float(v2),font=('helvetica', 10, 'bold'),bg='white')
    canvas1.create_window(210, 240, window=label7)
      
buttonDiv = Button(NewCalc, text='/', command=div, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 5)
canvas1.create_window(240, 190, window=buttonDiv)

NewCalc.mainloop()

