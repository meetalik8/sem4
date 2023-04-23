import tkinter as tk

root=tk.Tk()
root.title('RadioGaga')
root.geometry('500x500')
radio1= tk.Radiobutton(root,text='Slay',value=1).grid(column=0,row=0)
radio2= tk.Radiobutton(root,text='Flop',value=2).grid(column=0,row=1)
radio3= tk.Radiobutton(root,text='Ugly',value=3).grid(column=0,row=2)
root.mainloop()
