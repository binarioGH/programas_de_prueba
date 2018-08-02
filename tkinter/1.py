#-*-coding: utf-8 -*-
from tkinter import *
from random import randint




if __name__ == '__main__':
	tab = Tk()
	tab.title("Hola mundo 2")
	tab.geometry("{}x{}".format(randint(100,200), randint(100,200)))
	tab.mainloop()	
	