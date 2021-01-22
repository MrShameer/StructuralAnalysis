from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("350x300")

Label(top,text = "Input of first concentrated point load (i): ").place(x = 20,y = 20)
il = Entry(top,width = 10)
il.place(x=250,y=20)

Label(top,text = "Input of second concentrated point load (j): ").place(x = 20,y = 50)
jl = Entry(top, width = 10)
jl.place(x = 260,y = 50)

Label(top,text = "Input distance of point load i from A (x): ").place(x = 20,y = 80)
xl = Entry(top, width = 10)
xl.place(x = 250,y = 80)

Label(top,text = "Input distance of point load j from A (y): ").place(x = 20,y = 110)
yl = Entry(top, width = 10)
yl.place(x = 250,y = 110)

Label(top,text = "Distance of point C from A (c): ").place(x = 20,y = 140)
cl = Entry(top, width = 10)
cl.place(x = 240,y = 140)

Label(top,text = "Input of length of beam for section AB (l1): ").place(x = 20,y = 170)
l1l = Entry(top, width = 10)
l1l.place(x = 260,y = 170)

Label(top,text = "Input of length of beam for section BC (l2): ").place(x = 20,y = 200)
l2l = Entry(top, width = 10)
l2l.place(x = 260,y = 200)

def sets():
	global i,j,x,y,c,l1,l2
	try:
		i = float(il.get())
		j = float(jl.get())
		x = float(xl.get())
		y = float(yl.get())
		c = float(cl.get())
		l1 = float(l1l.get())
		l2 = float(l2l.get())
		return "go"
	except:
		return

def reactionAB():
	rb = (-j*y - i*x)/l1
	ra = -i-j-rb
	return "RA: " + str(ra) + "KN\nRB: " + str(rb)+"KN"

def internalshear():
	vc = 1-(x/l1)
	vc2 =  1 - y/l1
	c = -i*round(vc,2) - j*round(vc2,2)
	return "Internal shear force at point C: " + str(c)

def internalmoment():
	mc = 2-((2*x)/l1)
	mc2 = 2 - ((2*y)/l1)
	c = -i * round(mc,2)-j *round(mc2,2)
	return "Internal moment at point C: " + str(round(c,2))

def runs():
	if(sets()=="go"):
		messagebox.showinfo("Answers", reactionAB() + "\n\n" + internalshear() + "\n\n" + internalmoment())
	else:
		messagebox.showerror("Error", "Please make sure every field has been filled") 


submit_button = Button(top,text = "Calculate",command=runs).place(x = 120,y = 240) 
top.mainloop()
