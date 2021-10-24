# https://realpython.com/python-gui-tkinter/#check-your-understanding_1
import tkinter as tk

window = tk.Tk()
window.title('sprites test')
mlabel = tk.Label(text='Sprites Test', fg='yellow', bg='green').pack()

canvas = tk.Canvas(window, width=1000, height=1000, bg='white')

gif1 = tk.PhotoImage(file='sprite.gif')
id1 = canvas.create_image(500, 500, image=gif1)
canvas.pack(padx=10, pady=10)

canvas.mainloop()
window.mainloop()
