#-*-coding: utf-8-*-
import random
import subprocess

def fin(resultado):
	print("\n\n{}".format(resultado))
	exit()
if __name__ == '__main__':
	tnum = int()
	num = random.randint(1, 100)
	intentos = 0
	while tnum != num:
		if intentos == 10:
			fin("perdiste")
		subprocess.call(["cmd.exe", "/c", "cls"])
		if intentos >= 1:
			if tnum < num:
				mm = "menor"	
			else:
				mm = "mayor"
			print("el numero {} es {} al que debes adivinar".format(tnum, mm))
		print("intentos: {}".format(intentos))
		try:
			tnum = int(input("introduce un numero: "))
		except:
			continue
		intentos += 1
	fin("ganaste")
