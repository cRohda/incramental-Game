# https://realpython.com/python-gui-tkinter/#check-your-understanding_1
import tkinter as tk

window = tk.Tk()

for i in range(1, 6):
    window.columnconfigure(i, weight=1, minsize=30)
    window.rowconfigure(i, weight=1, minsize=25)
    for j in range(1, 6):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=3
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f'Row {i}\nColumn {j}')
        label.pack()

window.mainloop()