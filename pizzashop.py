from tkinter import * 
from tkinter.ttk import * 
import pyautogui
w,h = pyautogui.size()
screen = Tk()
screen.geometry(f"{w}x{h}")
screen.config(background="darkgreen",border=10,borderwidth=10,relief="raised")
screen.title("Lets buy pizza")

Label(screen,text="Welcome to Pizza Shop",font=("Arial",30),background="darkgreen",foreground="white").grid(row=0,column=0,columnspan=3,pady=20)
pizzaval = StringVar()
Label(screen,text="Select your pizza",font=("Arial",20),background="darkgreen",foreground="white").grid(row=1,column=1,pady=20)
pizzacombo = Combobox(screen,textvariable=pizzaval,values =["Marg","Meateor","BBQ,","Pepperoni"] ,font=("Arial",20),state="readonly")
pizzacombo.grid(row=2,column=1,pady=20)
pizzacombo.current(0)
Label(screen,text="Select your quantity",font=("Arial",20),background="darkgreen",foreground="white").grid(row=1,column=2,pady=20)
quantity = Spinbox(screen,from_=1,to=10,font=("Arial",20),width=5)
quantity.grid(row=2,column=2,pady=20)
Label(screen,text="Select the size",font=("Arial",20),background="darkgreen",foreground="white").grid(row=1,column=3,pady=20)
sizeval = StringVar(value="Medium")
Radiobutton(screen,text="Small     ",variable=sizeval,value="Small").grid(row=2,column=3,pady=20)
Radiobutton(screen,text="Medium",variable=sizeval,value="Medium").grid(row=3,column=3,pady=20)
Radiobutton(screen,text="Large     ",variable=sizeval,value="Large").grid(row=4,column=3,pady=20)

screen.mainloop()