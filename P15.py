import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk
root=tk.Tk()
root.title("Progress Bar")
root.geometry('500x500')
bar= Progressbar(root, length=200, style='black.Horizontal.TProgressbar')
bar['value']=80
bar.grid(column=0,row=0)
root.mainloop()
