#-*-coding: utf-8-*-
#-*-coding: utf-8 -*-
from random import randint
from getpass import getpass
from subprocess import call

if __name__ == '__main__':
	chose = int()
	opciones = ("tijeras","piedra", "papel", "tijera")
	points = 0
	pptpoints = 0
	while chose != 99:
		call(("cmd.exe","/c","cls"))
		chose = int(input('''
			PIEDRA, PAPEL O TIJERAS
			tu: {}  ppt: {}

			[1] piedra
			[2] papel
			[3] tijeras

			para salir: [99]

			> '''.format(points, pptpoints)))
		if chose == 99:
			continue
		pptchose = randint(-1, 2)
		getpass("Escogiste: {} y la computadora: {}...".format(opciones[chose], opciones[pptchose]))
		if pptchose > chose:
			pptpoints += 1
		elif pptpoints == chose:
			continue
		else:
			points += 1