import tkinter as tk
def hello_t():
    print("Hello!!!!!")
def bye_t():
    print("end this")
root = tk.Tk()
root.title("GUI 1")
butt1=tk.Button(text="Hello",bg="red",command=hello_t)
butt1.grid(column=0,row=0)
butt1=tk.Button(text="Bye",bg="green",command=bye_t)
butt1.grid(column=3,row=0)

root.mainloop()
