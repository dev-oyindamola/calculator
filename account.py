import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import time
import backend as bk
import password as pa
# import cons
import random as ra
import bcrypt




window = tk.Tk()
window.geometry("1200x700")
# window.config(bg="red")
window.title("My personal doc")


def com():
	get = empty.get()
	get_emp = emp.get()
	get_la = la.get()
	get_lebel = lebel.get()
	get_lebel_ = bytes(lebel_.get(),encoding="utf-8")
	get_code = code.get()
	bye = bcrypt.hashpw(get_lebel_,bcrypt.gensalt())
	
	if len(get) == 0 or len(get_emp) == 0 or len(get_la) == 0 or len(get_lebel) == 0 or len(get_lebel_) ==0 or len(get_code) == 0:
		messagebox.showerror(title="Error", message="Please fill all and your number must be 11 digel and password must be bewteen 8 and 15")
		empty.delete(0, END)
		emp.delete(0, END)
		la.delete(0, END)
		lebel.delete(0, END)
		lebel_.delete(0, END)
		code.delete(0, END)
		empty.focus()
		emp.focus()
		code.focus()
		lebel_.focus()
		la.focus()
		lebel.focus()
		
	elif len(get_la) == 11 or len(get_lebel_) >= 8 :
		bk.create_password(get,get_emp,get_la,get_lebel,get_lebel_,get_code)
		messagebox.showinfo(title="success",message="Successful")
		empty.focus()
		emp.focus()
		code.focus()
		lebel_.focus()
		lebel_.focus()
		la.focus()
		lebel.focus()
		window.destroy()
		time.sleep(0.0)
		import  myperdoc
		
		
	

def gen():
	# get = int(code.get())
	data= pa.genarate_password()
	code.delete(0, END)
	code.insert(tk.END,data)


fram = tk.Frame(width=1500,height=700) 
fram.pack()
fram.place(anchor="center",relx=0.5, rely=0.5)
log = ImageTk.PhotoImage(Image.open("doc9.jpg"))
labe = tk.Label(fram, image=log)
labe.place(x=0,y=-130)


e = Label(background="white")
em = Label(background="white")
emo = Label(background="white")
empt = Label(background="white")
empty_= Label(background="white")
empty_l = Label(background="white")
empty_la = Label(background="white")
empty_lab = Label(background="white")
empty_labes = Label(background="white")
empty_label = Label(background="white")
empty_labe = Label(background="white")



def show():
	show_button = Button(image=show_image, command=hide, relief=FLAT, activebackground="white",bd=0,bg="white")
	show_button.place(x=837,y=364)
	lebel_.config(show='')
def hide():
	hide_button = Button(image=hide_image, command=show, relief=FLAT, activebackground="white",bd=0,bg="white")
	hide_button.place(x=837,y=364)
	lebel_.config(show='*')


show_image = ImageTk.PhotoImage(Image.open("show.png"))
hide_image = ImageTk.PhotoImage(Image.open("hide.png"))



empty=Entry(font=10, width=40, justify="center")
emp=Entry(font=10, width=40, justify="center")
la = Entry(font=10,width=40,justify="center")
lebel = Entry(font=10,width=40,justify="center")
lebel_ =Entry(window,highlightthickness=2.4,bd=2.4,bg="white",fg='black',show="*", relief=FLAT,font=("",10))
code = Entry(font=10,width=40,justify="center")

show_button = Button(image=hide_image, command=show, relief=FLAT, activebackground="white",bd=0,bg="white")
show_button.place(x=837,y=364)


label=Label(text="First Name", font=17,bg="blue")
label2 = Label(text="Last Name", font=17,bg="blue")
number = Label(text="Phone number", font=17,bg="blue")
user = Label(text="User name", font=17,bg="blue")
password = Label(text="Password", font=17,bg="blue")
cod = Label(text="Code", font=17,bg="blue")


den= Label(background="red")
dan=Label(background="red")
dean=Label(background="red")


sing = Button(text="Sign in",font=("Algerian",10,"normal"),bg="white",command=com)
generatetor = Button(text="Generate",font=("Algerian",10,"normal"),bg="white",command=gen)



code.place(x=466,y=430)


generatetor.place(x=835,y=430)
cod.place(x=420,y=430)

label.place(x=384, y=209)
empty.place(x=470,y=209)
label2.place(x=384, y=252)

user.place(x=384,y=340)
password.place(x=390,y=379)
number.place(x=360,y=295)
emp.place(x=470,y=256)
la.place(x=470,y=296)
lebel.place(x=470,y=339)
lebel_.place(x=470,y=379,width=364)
sing.place(x=620,y=470)






window.mainloop()
