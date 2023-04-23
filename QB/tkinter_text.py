import tkinter as tk
root=tk.Tk()
root.title("Text widhget")
mytext=tk.Text(root)
mytext.insert('1.0',"Python excercise")
mytext.insert('1.20','Practicing')
mytext.delete('1.0')
mytext.delete('end - 2 chars')
mytext.pack()

root.mainloop()
