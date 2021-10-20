import tkinter as tk

while True:
    window = tk.Tk()
    window.title('You are infected')
    window.configure(width=500, heigh=300)
    window.configure(bg='red')
    label = tk.Label(
        text='you are infected with many virus',
        fg='black',
        bg='red',
        width=1000,
        height=20
    )
    CCN = tk.Label(
        text='enter your credit card number to clean your computer:',
        fg='black',
        bg='red',
        width=500,
        height=3
    )
    CC = tk.Entry(
        bg='white',
        fg='black',
        width=500
    )
    label.pack()
    CCN.pack()
    CC.pack()
    window.mainloop()
