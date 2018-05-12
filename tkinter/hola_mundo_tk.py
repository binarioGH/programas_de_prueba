#-*-coding: utf-8-*-
# https://www.youtube.com/watch?v=iPXiZALnZFg
import tkinter
if __name__ == '__main__':
	ventana = tkinter.Tk()
	ventana.title("Hola, mundo")
	ventana.geometry("380x300")
	ventana.configure(background="snow")
	texto1 = tkinter.Label(ventana, text="Esta es mi primer ventana.", bg="black", fg="white")
	texto1.pack(fill=tkinter.X)
	texto2 = tkinter.Label(ventana, text="Espero mejorar en esto", bg="white", fg="black")
	texto2.pack()
	ventana.mainloop()
