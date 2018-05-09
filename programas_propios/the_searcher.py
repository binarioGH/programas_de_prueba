#-*- coding: utf-8-*-
from sys import argv 
import os

def search(file):
	dirs = []
	for f in os.listdir():
		if os.path.isdir(f):
			dirs.append(f)
			continue
		else:
			if f == file:
				print("\n \nse ha encontrado el archivo '{}'' en \n\n'{}'".format(file, os.getcwd()))
				exit()
	return dirs

if __name__ == '__main__':
	if len(argv) != 3:
		print("este programa ocupa 3 argumentos para funcionar.")
		print("the_shearcher.py (directorio en el que se busca) (archivo que buscas)")
		exit()
	else:
		try:
			os.chdir(argv[1])
			od = os.getcwd()
		except:
			print("el directorio '{}' no se ha encontrado.".format(argv[1]))
		else: 
			dirs = search(argv[2])
			for d in dirs:
				try:
					os.chdir(d)
				except:
					print("no se pudo revizar el directorio '{}'".format(d))
					continue
				else:
					search(argv[2])
					os.chdir(od)
			