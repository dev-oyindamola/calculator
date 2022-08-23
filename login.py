import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import time
import backend as bk
import time




	
window = tk.Tk()
window.config(bg="#a55df0", pady=50, padx=50)
window.resizable(width=False,height=False)
window.title("My personal doc")





log1 = ImageTk.PhotoImage(Image.open("doc11.jpg"))
canvas = tk.Canvas(width=400, height=600,bg="#a5500c")
canvas.create_image(200, 300, image=log1)
canvas.grid(row=0, column=2, rowspan=6, padx=40)





def log():
	car = empty.get()
	dog = lebel_.get()

		
	if len(car) != 0 and len(dog) != 0:
		text.delete("1.0","end-1c")
		text.insert(tk.END,"invail password or number")	
		empty.focus()
		lebel_.focus()
	if len(car) == 0 and len(dog) == 0 :
		text.delete("1.0","end-1c")
		text.insert(tk.END,"please fill all")	
	if bk.get_data(car,dog):
		sir = bk.get_data(car,dog)
		empty.focus()
		lebel_.focus()
		empty.delete(0, END)
		lebel_.delete(0, END)
		# empty.insert(tk.END,sir)
		window.destroy()
		time.sleep(0.0)
		import myperdoc	



def sign():
	window.destroy()
	time.sleep(0)
	import account




car = """
Welcome to my personal doc\n
please input the number you use to register\n
in the number in the empty place\n
your account and then input your password in the\n
other empty place if you follow the following step \n
have a good health thank you for chooseing MY PERSONAL DOC

"""


def show():
	hide_button = Button(lebel_,image=show_image, command=hide, relief=FLAT, activebackground="white",bd=0,bg="white")
	hide_button.place(x=226,y=-17)
	lebel_.config(show='')
def hide():
	show_button = Button(lebel_,image=hide_image, command=show, relief=FLAT, activebackground="white",bd=0,bg="white")
	show_button.place(x=226,y=-17)
	lebel_.config(show='*')


show_image = ImageTk.PhotoImage(Image.open("show.png"))
hide_image = ImageTk.PhotoImage(Image.open("hide.png"))




empty=Entry(font=10,width=30, justify="center")
lebel_ =Entry(window,highlightthickness=2.4,bd=2.4,bg="white",fg='black', relief=FLAT,show="*",font=("",10))
# password_entry.pack(pady=200)


show_button = Button(lebel_,image=hide_image, command=show, relief=FLAT, activebackground="white",bd=0,bg="white")
show_button.place(x=226,y=-17)


create = Button(text="Create account",underline=20,font=("Courier",12,"bold"),bg="#a55df0",command=sign)
text=Text(width=20,height=5, font=("Algerian",10,"bold"),bg="#a55df0")
login = Button(text="Login",font=("Courier",10,"bold"),bg="#a55df0",command=log)
email = Label(text="Email: ",font=("Arial",12,"normal"),bg="#a55df0")
password = Label(text="Password:",font=("Arial",12,"normal"),bg="#a55df0")
message = Label(text=car,font=("Arial black",12,"bold"),bg="#a55df0")





login.place(x=360,y=450)
message.grid(row=0, column=0, columnspan=2)
email.place(x=200,y=350)
password.place(x=170,y=380)
empty.place(x=260,y=350)
lebel_.place(x=260,y=380,height=20,width=274)
text.place(x=309,y=490)
create.place(x=309,y=590)



window.mainloop()