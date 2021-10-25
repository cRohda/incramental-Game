# https://realpython.com/python-gui-tkinter/#check-your-understanding_1
import tkinter as tk

def click():
    value = int(money["text"])
    money["text"] = f"{value + 1}"

window = tk.Tk()
window.title('BC High Clicker')
window.configure(bg='white')

picture = tk.PhotoImage(file='Logo.png')
tutorial = tk.PhotoImage(file='Instructions.png')
price = tk.PhotoImage(file='Price.png')

instructions = tk.Label(image=tutorial)
btn = tk.Button(image=picture, command=click)
money = tk.Label(text='0',bg='white', fg='black')
sign = tk.Label(image=price)

instructions.grid(row=0, column=0, sticky='w')
btn.grid(row=1, column=0, sticky='nsew')
sign.grid(row=0, column=1)


window.mainloop()