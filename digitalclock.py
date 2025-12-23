from tkinter import *
from time import strftime

root = Tk()

root.resizable(0,0)
root.title("Python Digital Clock")
root.geometry("500x150") 


Label(root, text='Python Digital Clock', font=('Arial', 12, 'bold')).pack(pady=5)

mark = Label(root, font=('calibri', 50, 'bold'), background='black', foreground='cyan')
mark.pack(anchor='center', fill='both', expand=1, padx=20, pady=10)


def Dclock():

    string = strftime('%H:%M:%S %p')
    
    
    mark.config(text=string)

    mark.after(1000, Dclock)
Dclock()
root.mainloop()
