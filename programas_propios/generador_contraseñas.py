#-*-coding: utf-8-*-
import random
import os

if __name__ == '__main__':
	choice = str()
	print("introduzca el nombre del archivo en el que quiera guardad su clave. \n{}".format(os.getcwd()))
	name = str(input("\n>"))
	print("introduzca la cantidad maxima de caracteres en su clave.")
	maxim = int(input("\n>"))
	print("introduzca la cantidad minima de caracteres en su clave.")
	minim = int(input("\n>"))
	passwr = str()
	chars = ("#","&"," ","1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z")
	for char in range(random.randint(minim,maxim)):
		passwr += random.choice(chars)
	file = open(name, "w")
	file.write(passwr)
	file.close()


