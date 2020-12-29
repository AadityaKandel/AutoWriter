from tkinter import *
import pyautogui as pp
import keyboard
import time

root = Tk()

root.title("AutoWriter By Aaditya Kandel")
root.maxsize(870,800)
root.minsize(870,800)

Label(text = "Welcome To AutoWriter",bg = "black",fg = 'white',font = "comicsansms 21 bold").pack()
Label(text = "",bg = "black",fg = 'white',font = "comicsansms 1 bold").pack()
def acttt():
	for i in range(0,999999999):
		root.update()
		if keyboard.is_pressed(f"{(shrt.get())}"):
			root.update()
			time.sleep(eval((aft.get())))
			for i in range(0,(repeat.get())):
				root.update()
				pp.write(f'''{(text1.get(1.0, END))}''',interval = (delay.get()))
				act.set("Activate")
				root.title("Work Done")
			break
def actt():
	act.set('Activated')
	if (shrt.get()) == "none" or (shrt.get()) == "None":
		root.update()
		time.sleep(eval((aft.get())))
		for i in range(0,(repeat.get())):
			root.update()
			pp.write(f'''{(text1.get(1.0, END))}''',interval = (delay.get()))
			act.set("Activate")
			root.title("Work Done")
	else:
		acttt()

f1 = Frame(borderwidth = 0,bg = "black")
f2 = Frame(borderwidth = 0,bg = "black")
f3 = Frame(borderwidth = 0,bg = "black")

Label(f1,text = " ShortCut Key: ",bg = "black",fg = 'white',font = "comicsansms 14 bold",borderwidth = 0).pack(side = LEFT)
shrt = StringVar()
shrt.set("None")
Entry(f1,textvariable = shrt,bg = "black",fg = 'white',font = "comicsansms 14 bold",width = 10).pack(side = LEFT)
Label(f1,text = "    ",bg = "black",fg = 'white',font = "comicsansms 14 bold",borderwidth = 0).pack(side = LEFT)

Label(f1,text = " After Time: ",bg = "black",fg = 'white',font = "comicsansms 14 bold",borderwidth = 0).pack(side = LEFT)
aft = StringVar()
aft.set("3")
Entry(f1,textvariable = aft,bg = "black",fg = 'white',font = "comicsansms 14 bold",width = 10).pack(side = LEFT)
Label(f1,text = "   seconds",bg = "black",fg = 'white',font = "comicsansms 11 bold",borderwidth = 0).pack(side = LEFT)

Label(f3,text = " Time Delay: ",bg = "black",fg = 'white',font = "comicsansms 14 bold",borderwidth = 0).pack(side = LEFT)
delay = DoubleVar()
delay.set(0.25)
Entry(f3,textvariable = delay,bg = "black",fg = 'white',font = "comicsansms 14 bold",width = 10).pack(side = LEFT)
Label(f3,text = " seconds     ",bg = "black",fg = 'white',font = "comicsansms 11 bold",borderwidth = 0).pack(side = LEFT)

Label(f3,text = " Repeat: ",bg = "black",fg = 'white',font = "comicsansms 14 bold",borderwidth = 0).pack(side = LEFT)
repeat = IntVar()
repeat.set(1)
Entry(f3,textvariable = repeat,bg = "black",fg = 'white',font = "comicsansms 14 bold",width = 10).pack(side = LEFT)
Label(f3,text = " times",bg = "black",fg = 'white',font = "comicsansms 11 bold",borderwidth = 0).pack(side = LEFT)

f1.pack(anchor = W)
Label(text = "",bg = "black").pack()
f3.pack(anchor = W)

Label(text = "",bg = "black").pack()
act = StringVar()
act.set('Activate')
Button(textvariable = act,bg = "black",fg = "white",font = "comicsansms 14 bold",command = actt).pack()
Label(text = "",bg = "black").pack()

Label(text = "What To Write [ Give Below ]",bg = "black",fg = 'white',font = "comicsansms 15 bold").pack()
Label(text = "",bg = "black",fg = 'white',font = "comicsansms 14 bold").pack()

s = Scrollbar(root)
s.pack(fill = "y", side = "right")

textvar = StringVar()
text1 = Text(root,yscrollcommand =s.set,font = "comicsansms 20 italic",bg = "black",fg = "white")

text1.pack(fill = BOTH)

s.config(command = text1.yview)
root.config(bg = "black")
root.mainloop()