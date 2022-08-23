import tkinter as tk
from tkinter import *


window = tk.Tk()
window.geometry("300x400")
window.config(bg="blue")
window.resizable(width=False,height=False)
# window.tk.call("wm","iconphoto",window._w,tk.PhotoImage(file='C:/Users/USER/Desktop/pass/'))

window.title("Calculator")

e1 = StringVar()
empty_label = Label(background="blue")
entry = Entry(font=10, width=20, justify="center", textvariable=e1)

def reset_all():
	global expression
	expression = ""
	e1.set("")

expression =""
def reset():
	global expression
	expression = "1"
	e1.set("")
def prass(num):
	global expression

	expression += str(num or entry.get())
	e1.set(expression)

def equal():
	try:

		global expression
		result = str(eval(expression or entry.get()))

		e1.set(result)
		expression = ""
	except:
		e1.set("matherror")	
		expression=""
# def factoria(n):
# 	global expression

# 	ft=e1.get()
# 	if ft < 0 or user==0:
# 		print("no factorial for negative")
# 	else:
# 		num = 1
# 		while (n > 1):
# 			num *= n
# 			n -= 1
# 		return num
	

	

	
# user = int(input("Enter your number:"))	
	# e1.set(expression)
# user = int(input("Enter your number:"))	

x= "*"
namb = Button(text="1", font=10, bg="gold",command=lambda:prass(1))
numb2 = Button(text="2", font=10, bg="gold",command=lambda:prass(2))
numb3 = Button(text="3", font=10, bg="gold",command=lambda:prass(3))
numb4 = Button(text="4", font=10, bg="gold",command=lambda:prass(4))
numb5 = Button(text="5",font=10, bg="gold",command=lambda:prass(5))
numb6 = Button(text="6",font=10, bg="gold",command=lambda:prass(6))
numb7 = Button(text="7",font=10, bg="gold",command=lambda:prass(7))
numb8 = Button(text="8",font=10, bg="gold",command=lambda:prass(8))
numb9 = Button(text="9",font=10, bg="gold",command=lambda:prass(9))
numb0 = Button(text="0",font=10, bg="gold",command=lambda:prass(0))
numbx = Button(text="x",font=10, bg="gold",command=lambda:prass(x))
numbd = Button(text="/",font=15, bg="gold",command=lambda:prass("/"))
numba = Button(text="+",font=10, bg="gold",command=lambda:prass("+"))
numbs = Button(text="-",font=10, bg="gold",command=lambda:prass("-"))
numbf = Button(text="//",font=10, bg="gold",command=lambda:prass("//"))
numbp = Button(text= "%",font=10, bg="gold",command=lambda:prass("%"))
numbxr = Button(text=".",font=10,bg="gold",command=lambda:prass("."))
factoria = Button(text="Factorial",font=10,bg="gold")
numbxy = Button(text="c",font=15,bg="red", command=reset_all)
numbxu = Button(text="=",font=20,bg="gold",command=equal)

factoria.place(x=100,y=310)
empty_label.pack()
entry.pack()
namb.place(x=60,y=130)
numb2.place(x=100,y=130)
numb3.place(x=140,y=130)
numb4.place(x=180,y=130)
numbx.place(x=155,y=270)
numb5.place(x=60,y=180)
numb6.place(x=100,y=180)
numb7.place(x=140,y=180)
numb8.place(x=180,y=180)
numbd.place(x=220,y=180)
numba.place(x=60,y=230)
numb9.place(x=100,y=230)
numb0.place(x=140,y=230)
numbs .place(x=180,y=230)
numbf.place(x=220,y=230)
numbp.place(x=73,y=270)
numbxr.place(x=117,y=270)
numbxy.place(x=220,y=130)
numbxu.place(x=199,y=270)






window.mainloop()







