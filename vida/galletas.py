#-*-coding: utf-8 -*-
from random import choice
# Este programa sale de un día que mí tía me preguntó si quería algo de la tienda y le dije que 
# quería chokis, cualquier tipo de chokis menos las moradas, entonces pensé en el algoritmo.
if __name__ == '__main__':
	galletas = ("chokis moradas", "chokis rojas", "chokis normales")
	choose = galletas[0]
	while choose == galletas[0]:
		choose = choice(galletas)
	print("te traje {}".format(choose))
	
