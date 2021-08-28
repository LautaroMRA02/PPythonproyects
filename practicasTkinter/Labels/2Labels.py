import tkinter as tk 

window  =   tk.Tk()

label   =   tk.Label(
    text=   "Hello Tkinder",
    fg  =   "white",
    bg  =   "black",
    width=  10,             #creo que funciona como %
    height= 100

)
label.pack()


window.mainloop()
