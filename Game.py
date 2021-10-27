import tkinter as tk
import webbrowser
from time import sleep


def click():
    value = int(money["text"])
    money["text"] = f"{value + 1}"

def rickroll():
    url = 'https://www.youtube.com/watch?v=x31tDT-4fQw'
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)

def p1():
    if int(money['text']) >= 50:
        p1loss = int(money['text'])
        money['text'] = f'{p1loss - 50}'
        while True:
            acvalue = int(money['text'])
            money['text'] = f'{acvalue + 1}'
            sleep(5)


window = tk.Tk()
window.title('BC High Clicker')
window.configure(bg='white')

# Images
picture = tk.PhotoImage(file='Logo.png')
tutorial = tk.PhotoImage(file='Instructions.png')
price = tk.PhotoImage(file='Price.png')
mouse = tk.PhotoImage(file='Power1.png')

# Labels and Buttons
instructions = tk.Label(image=tutorial)
btn = tk.Button(image=picture, command=click)
money = tk.Label(text='0',bg='white', fg='black', font='verdana')
sign = tk.Label(image=price)
P1 = tk.Button(image=mouse, bg='white', command=p1)

# Griding
instructions.grid(row=0, column=0, sticky='w')
btn.grid(row=2, column=0, sticky='w')
sign.grid(row=0, column=1)
money.grid(row=0, column=3)
P1.grid(row=3, column=0, sticky='w')

window.mainloop()
