import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import time
import backend2 as bk






 
window =tk.Tk()
window.config(bg="#0d50bc")
window.geometry("1300x700")
window.title("my personal doc")

def __init__(self):
	pass
index1=""
# index2 =""
def sub():
	data = diseases.get()
	get_data = symptoms.get("1.0","end-1c")
	date = war.get("1.0",END)
	diseases.delete(0, END)
	symptoms.delete("1.0", END)
	war.delete("1.0", END)
	get_date = bk.create_diseases(data,get_data,date)

def back():
	window.destroy()
	time.sleep(0)
	import myperdoc

def com():
	window.destroy()
	time.sleep(0)
	import constact	
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="<--", command=back)
menubar.add_cascade(label="Comment", command=com)
window.config(menu=menubar)

exit = Button(text="Exit",font=("Arial",8,"normal"),bg="#0d50bc", command=window.quit,underline=100)

exit.place(x=1243,y=0,width=60)

fram = tk.Frame(width=370,height=700) 
fram.pack()
fram.place(anchor="center",relx=0.14, rely=0.5)
log = ImageTk.PhotoImage(Image.open("images8.jpeg"))
labe = tk.Label(fram, image=log)
labe.place(x=0,y=0)


symptoms = Text(font=10,width=50,relief=FLAT,selectbackground="#fd94cd",selectborderwidth=3,selectforeground="#cd4905")


diseases = Entry(font=10,width=40,justify="center",relief=FLAT,selectbackground="#fd94cd",selectborderwidth=3,selectforeground="#cd4905")
dis = Label(text="About",font=("Arial",10,"bold"),bg="#0d5dc0")
sym = Button(text="Submit",font=("Arial",10,"normal"),bg="#0d50bc", command=sub)
oyin = Label(text="Diseases",font=("Arial",10,"bold"),bg="#0d5dc0")
ore = Label(text="Symptoms",font=("Arial",10,"bold"),bg="#0d5dc0")
war = Text(font=10,width=100,relief=FLAT,selectbackground="#fd94cd",selectborderwidth=3,selectforeground="#cd4905")

scroll = tk.Scrollbar(window, orient=tk.VERTICAL, command=symptoms.yview)
symptoms.configure(yscrollcommand=scroll.set)
scroll.place(x=861,y=91,height=240)

scroll = tk.Scrollbar(window, orient=tk.VERTICAL, command=war.yview)
war.configure(yscrollcommand=scroll.set)
scroll.place(x=1271,y=370,height=250)



oyin.place(x=620,y=0)
diseases.place(x=470,y=30)
symptoms.place(x=460,y=90,width=400,height=240)
war.place(x=470,y=370,width=800,height=250)
dis.place(x=420,y=490)
ore.place(x=620,y=60)
sym.place(x=630,y=630)

window.mainloop()