import tkinter as tk

root=tk.Tk()
root.geometry('350x350')
root.title('SpinBox')
spin=tk.Spinbox(root,from_=0.6,to=50.0,increment=.01)
spin.pack(side=tk.RIGHT)
root.mainloop()
