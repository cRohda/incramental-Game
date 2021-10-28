import tkinter as tk
import webbrowser
from time import sleep


def click():
    value = float(wealth["text"])
    wealth["text"] = f"{value + 1}"

def rickroll():
    url = 'https://www.youtube.com/watch?v=x31tDT-4fQw'
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)

def p1():
    if float(wealth['text']) >= 40:
        p1loss = float(wealth['text'])
        wealth['text'] = f'{p1loss - 40}'

        ac_count = float(acamount['text'])
        acamount['text'] = f'{ac_count + 1}'

        ac_cps = float(pps['text'])
        pps['text'] = f'{ac_cps + 0.25}'
    else:
        overdraft()

def overdraft():
    print('Not enough money!')


window = tk.Tk()
window.title('Click The Pizza 3000')
window.geometry("800x1000")
window.configure(bg='white')

# Images
picture = tk.PhotoImage(file='Logo.png')
header = tk.PhotoImage(file='Title.png')
price = tk.PhotoImage(file='Price.png')
mouse = tk.PhotoImage(file='Power1.png')

# Labels
title = tk.Label(image=header, bg='white')
space = tk.Label(text="\n\n\n\n", bg='white')
sign = tk.Label(image=price, bg='white')
wealth = tk.Label(text='200', font=('Verdana', 69), bg='white', fg='black')
pps = tk.Label(text='0', font=('Verdana', 40), bg='white', fg='black')
acamount = tk.Label(text='0', font=('Verdana', 40), bg='white', fg='black')

# Buttons
logo = tk.Button(image=picture, command=click)
autoclick = tk.Button(image=mouse, bg='white', command=p1)

# Griding
title.grid(row=0, column=0)
pps.grid(row=1, column=0, sticky='n')
logo.grid(row=2, column=0, sticky='nsew')
sign.grid(row=1, column=1, sticky='e')
wealth.grid(row=1, column=2, sticky='w')
space.grid(row=3, column=0)
autoclick.grid(row=4, column=0, sticky='e')
acamount.grid(row=4, column=1, sticky='w')

window.mainloop()