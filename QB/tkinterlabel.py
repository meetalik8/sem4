import tkinter as tk
parent = tk.Tk()
parent.title("-Welcome to Python tkinter Basic exercises-")
my_label = tk.Label(parent, text="Hello", font=("Arial Bold", 70))
my_label.grid(column=0, row=0)
parent.mainloop()
