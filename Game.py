# https://realpython.com/python-gui-tkinter/#check-your-understanding_1
import tkinter as tk

def click():
    value = int(money["text"])
    money["text"] = f"{value + 1}"

frm_form = tk.Frame(relief=tk.RAISED)
frm_form.pack()

window = tk.Tk()
window.title('Clicker')

instructions = tk.Label(master=frm_form, text='Click the button to earn money!')
moneysign = tk.Label(master=frm_form, text='$')
money = tk.Label(master=frm_form, text='0')
lemonade = tk.Button(master=frm_form, text='click me', command=click)

instructions.grid(row=0, column=3, sticky='nsew')
moneysign.grid(row=0, column=5, sticky='e')
money.grid(row=0, column=6, sticky='w')
lemonade.grid(row=1, column=3)

window.mainloop()