#-*- coding: utf-8 -*-
# 4- Escribir una función que tome un carácter y devuelva True 
# si es una vocal, de lo contrario devuelve False.

# 'dvocal' significa 'detectar vocal'
def dvocal(char):
	boolv = False
	vocales = ["a","e","i","o","u"]
	if len(char) > 1:
		print("solo se puede ingresar 1 caracter")
	else:
		for c in vocales:
			if c == char or c.upper() == char:
				boolv = True
		if boolv == True:
			print("{} es una vocal".format(char))
		else:
			print("{} no es una vocal".format(char))
if __name__ == '__main__':
	try:
		car = str(raw_input("ingresa un caracter: "))
		dvocal(car)
	except Exception as e:
		print("ese no es un str")