import tkinter as tk
from functools import partial
def call_result(labelResult,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result=int(num1)+int(num2)
    labelResult.config(text="Result=%a"%result)
    return
root=tk.Tk()
root.title("Form")
root.geometry("400x500+300+200")
num1=tk.StringVar()
num2=tk.StringVar()
labelnum1=tk.Label(root,text="A").grid(row=1,column=0)
labelnum2=tk.Label(root,text="B").grid(row=2,column=0)
labelResult=tk.Label(root)
labelResult.grid(row=3,column=0)
entrynum1=tk.Entry(root,textvariable=num1).grid(row=1,column=2)
entrynum2=tk.Entry(root,textvariable=num2).grid(row=2,column=2)
call_result=partial(call_result,labelResult,num1,num2)
buttoncal=tk.Button(root,text="Calculate",command=call_result).grid(row=4,column=0)
root.mainloop()

