import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import time
import backend2 as bk
import os






window =tk.Tk()
window.geometry("1350x700")
window.config(bg="#4444bb")
window.title("my personal doc")
window.resizable(width=False,height=False)


	# 
def dis_text():
	searc = empty.get().lower()
	if not bk.get_date(searc):
		text.delete("1.0", END)
		text.insert(tk.END,"not found")
	try:
		
		dat = bk.get_date(searc)
		text.insert(tk.END,dat)
	except tk._tkinter.TclError:
		pass
def add():
	window.destroy()
	time.sleep(0.0)
	import add

def gen():
	window.destroy()
	time.sleep(0.0)
	import myperdoc

def tor():
	window.destroy()
	time.sleep(0.0)
	import constact

def gan():
	window.destroy()
	time.sleep(0.0)
	import login


fram = tk.Frame(width=429,height=230) 
fram.pack()
fram.place(anchor="center",relx=0.0, rely=0.3)
log = ImageTk.PhotoImage(Image.open("images12.jpeg"))
labe = tk.Label(fram, image=log)
labe.place(x=204,y=0)


fra = tk.Frame(width=435,height=221) 
fra.pack()
fra.place(anchor="n",relx=0.0, rely=0.6)
lo = ImageTk.PhotoImage(Image.open("images2.png"))
label = tk.Label(fra, image=lo)
label.place(x=210,y=-10)



frame = tk.Frame(width=220,height=230) 
frame.pack()
frame.place(anchor="nw",relx=0.81, rely=0.6)
logo = ImageTk.PhotoImage(Image.open("images11.jpeg"))
labelse = tk.Label(frame, image=logo)
labelse.place(x=0,y=0)
# n, ne, e, se, s, sw, w, nw, or center


frames = tk.Frame(width=220,height=230) 
frames.pack()
frames.place(anchor="sw",relx=0.81, rely=0.5)
logos = ImageTk.PhotoImage(Image.open("images9.jpeg"))
labels = tk.Label(frames, image=logos)
labels.place(x=0,y=-1)

empty=Entry(font=10, width=80, justify="center")
empty.place(x=320,y=16)
text = Text(window, height=40, width=85,font=("Arial black",10,"bold"),bg="#4444bb")
text.place(x=305,y=70)


scroll = tk.Scrollbar(window, orient=tk.VERTICAL, command=text.yview)
text.configure(yscrollcommand=scroll.set)
scroll.place(x=1332,y=0,height=690)

var = IntVar()
for rext, value in [("Exit",1)]:	
	Radiobutton(window, text=rext, value=value,bg="#0d50bc", variable=vars,indicatoron=False,command=window.quit).place(x=1250,y=0,width=80)
var.set(10)



menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Add Diseases", command=add,underline=20)
menubar.add_cascade(label="Comment", command=tor)
menubar.add_cascade(label="Animal")
menubar.add_cascade(label="Search by Diseases",command=gen)
menubar.add_cascade(label="log out",command=gan)

window.config(menu=menubar)




search = Button(text="Search",font=("Algerian",10,"normal"),bg= "#05dcb9", command=dis_text )


search.place(x=1050,y=14,width=60)

window.mainloop()