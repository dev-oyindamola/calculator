import tkinter as tk
from tkinter import *
import time


window = tk.Tk()
window.geometry("1300x700")
window.config(bg="#a550f0")
window.resizable(width=False,height=False)
window.title("My personal doc")





def comma():
	window.destroy()
	time.sleep(0.000)
	import account
	

def yin():
	window.destroy()
	time.sleep(0)
	import login


log=Button(text="login",font=("Algerian",20, "normal"),bg="#a550f0",command=yin)
signup = Button(text="Sign up",font=("Algerian",20, "normal"),bg="#a550f0", command=comma)
# empty_label = Label(background="blue")
wel = Label(text="WELCOME TO MY PERSONAL DOC",font=("Algerian",40,"bold"),bg="#a550f0")
your = Label(text="Your health is pride",font=("Algerian",20,"bold"),bg="#a550f0")
# empty_label.pack()
log.place(x=2.3, y= 100)
signup.place(x=2.3,y= 300)
wel.pack()
your.pack()
# log.place(x=)






window.mainloop()