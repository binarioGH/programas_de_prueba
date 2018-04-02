#-*-coding: utf-8 -*-
# Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a"
# tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
# Se puede hacer que el usuario sea quien elija la palabra
if __name__ == '__main__':
	word = str(raw_input("introduzca una palabra: "))
	vocales = ["a","e","i","o","u"]
	counta = 0
	counte = 0
	counti = 0
	counto = 0
	countu = 0
	for letra in word:
		for vocal in vocales:
			if letra == vocal or letra == vocal.upper():
				if vocal == "a":
					counta += 1
				elif vocal == "e":
					counte += 1
				elif vocal == "i":
					counti += 1
				elif vocal =="o":
					counto += 1
				elif vocal == "u":
					countu += 1
	print('''
		{} : {}
		{} : {}
		{} : {}
		{} : {}
		{} : {}
		'''.format(vocales[0], counta, vocales[1], counte, vocales[2], counti, vocales[3], counto, vocales[4], countu))

