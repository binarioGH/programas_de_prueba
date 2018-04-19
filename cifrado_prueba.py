#-*- coding: utf-8 -*-
#NO USES ESTO COMO UN CIFRADO REAL, ES EXTREMADAMENTE DEBIL
import subprocess
#NO USES ESTO COMO UN CIFRADO REAL, ES EXTREMADAMENTE DEBIL
letterlist = (" ","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
Cyphlist = (" ","1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r")


def cyph(list1, list2, word):
	r_word = str()
	for letter in word:
		count = 0
		for l in list1:
			if letter == l or letter.upper() == l.upper():
				r_word += list2[count]
			else:
				count += 1
	return r_word

if __name__ == '__main__':
	d = str()
	while d != "s":
		subprocess.call(["cmd.exe","/c","cls"])
		d = input('''
		# NO USES ESTO COMO UN CIFRADO REAL, ES EXTREMADAMENTE DEBIL
		
		[c]ifrar
		[d]ecifrar
		[s]alir

		> ''')
		if d == "c" or d == "C":
			word = input("introduzca una palabra: ")
			new_word = cyph(letterlist, Cyphlist, word)
			print("la palabra cifrada es: {}".format(new_word))
			subprocess.call(["cmd.exe","/c","pause"])
		elif d == "d" or d == "D":
			word = input("introduzca la palabra cifrada: ")
			new_word = cyph(Cyphlist, letterlist, word)
			print("la palabra decifrada es: {}".format(new_word))
			subprocess.call(["cmd.exe","/c","pause"])

