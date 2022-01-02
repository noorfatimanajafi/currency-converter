from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from forex_python.converter import CurrencyRates
cr = CurrencyRates()


win = Tk()
win.title("Currency Converter")
win.minsize(width=1000, height=500)
win.maxsize(width=1000, height=500)

bg_img= PhotoImage(file=r"C:\Users\HP\Desktop\mytkpractice\mystock.png")
background_img = Label(win, image=bg_img)
background_img.place(x=0, y=0, relwidth=1, relheight=1)

from_lbl = Label(win, text="Convert From", font=('Helvetica', 20), bg="black", fg="white")
from_lbl.place(x=50, y=50)
from_com = ttk.Combobox(win, font=('Helvetica', 20), width=10)
from_com['values'] = ('INR', 'USD', 'CNY', 'CAD')
from_com.place(x=250, y=50)

to_lbl = Label(win, text="Converted To", font=('Helvetica', 20), bg="black", fg="white")
to_lbl.place(x=450, y=50)
to_com = ttk.Combobox(win, font=('Helvetica', 20), width=10)
to_com['values'] = ('INR', 'USD', 'CNY', 'CAD')
to_com.place(x=650, y=50)

amout_lbl = Label(win, text="Enter Amount", font=('Helvetica', 20), bg="black", fg="white")
amout_lbl.place(x=150, y=150) 
amount_field = Entry(win, font=('Helvetica', 20), bd=5)
amount_field.place(x=350, y=150)

def convert_amount():
    amount = amount_field.get()
    from_currency = from_com.get()
    to_currency = to_com.get()
    
    converted_amount = cr.convert(from_currency,to_currency,float(amount))
    result_lbl = Label(win, text="Converted Amount", font=('Helvetica', 20), bg="black", fg="white")
    result_lbl.place(x=200, y=250)
    result_value = Label(win, text=converted_amount, font=('Helvetica', 20), bg="black", fg="white")
    result_value.place(x=520, y=250)
    
con_btn = Button(win, text="Convert",  font=('Helvetica', 15), bg="green", fg="black", bd=2, command=convert_amount)
con_btn.place(x=700, y=150)

def get_rates():
    from_currency = from_com.get()
    to_currency = to_com.get()
    Currency = cr.get_rate(from_currency,to_currency)
    result_txt = f"Rate of {from_currency} into {to_currency} is {Currency}"
    messagebox.showinfo("Converted Currency", result_txt)

rates_btn = Button(win, text="Get Rates",  font=('Helvetica', 15), bg="green", fg="black", bd=2, command=get_rates)
rates_btn.place(x=850, y=50)

win.mainloop()