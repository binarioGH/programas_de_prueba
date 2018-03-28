#-*-coding: utf-8 -*-
# Escribir un programa que le diga al usuario que ingrese una cadena. El programa 
# tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene. 
if __name__ == '__main__':
	mayuscount = 0
	string = str(raw_input("introduzca una cadena de texto: "))
	for i in string:
		if i == i.upper() and i != " ":
			mayuscount += 1
	print("hay {} mayusculas en el texto".format(mayuscount))