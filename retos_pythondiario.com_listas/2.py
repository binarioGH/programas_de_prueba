#-*-coding: utf-8-*-
import random
#he modificado el segundo reto de http://www.pythondiario.com/2014/09/ejercicios-de-listas-en-python.html
#porque es un reto muy raro, te pide que hagas 2 funciones que hacen practicamente lo mismo.

def eliminar(lst):
	lst.pop(0)
	lst.pop(len(lst) - 1)
	return lst

def media(lst):
	lst = eliminar(lst)
	print(lst)
	prom = sum(lst)
	prom /= len(lst)
	return prom



if __name__ == '__main__':
	lista = []
	while len(lista) < random.randint(5, 15):
		lista.append(random.randint(1, 20))
	print(lista)
	lista = eliminar(lista)
	print(lista)
	promedio = media(lista)
	print("la media es: {}".format(promedio))