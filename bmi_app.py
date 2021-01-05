"Calculate BMI of as per inputs"

import tkinter as tk
bg = '#f1c159'
fg = '#2b2b2b'

root = tk.Tk()
root.geometry('588x488')
root.configure(bg= bg)
root.title("Bmi App: @_ace.python_(IG)")

w_var = tk.IntVar()
h_var = tk.IntVar()
bmi_var = tk.IntVar()


label_1 = tk.Label(root, text ='Enter your weight', font=('',15), fg=fg).place(x= 30, y= 18)
label_2 = tk.Label(root, text ='Enter your height', font=('',15), fg=fg).place(x= 30, y= 54)

#label_3 = tk.Label(root, text ='Your BMI is', font=('',10), fg=fg).place(x= 30, y=150)

entry_1 = tk.Entry(root,textvariable=w_var,font=('',15)).place(x= 200,y=18)
entry_2 = tk.Entry(root,textvariable=h_var,font=('',15)).place(x= 200,y=54)

label_4 = tk.Label(root,textvariable= bmi_var, font=('',10), fg=fg).place(x= 30, y=150)

def my_calc():

    weight = float(w_var.get())
    height = float(h_var.get())

    bmi = weight/(height**2)

    bmi_var.set(bmi)


b = tk.Button(root, text='Enter', font=30,command= my_calc ,fg=fg).place(x=225,y=100)

root.mainloop()