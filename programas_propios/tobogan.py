#-*-coding: utf-8 -*-
import random
import time
import subprocess
# este programa es una simulación de un guardia de tobógan 	en un parque acuatico, este intenta adivinar en cuanto
# tiempo va a llegar el siguiente niño y su edad.
def promedio(total):
	rtotal = int()
	for i in total:
		rtotal += i
	rtotal /= len(total)
	return rtotal

if __name__ == '__main__':
	timelist = []
	agelist = []
	while len(agelist) < 10:
		cooldown = random.randint(1, 10)
		edad = random.randint(5, 15)
		time.sleep(cooldown)
		subprocess.call(["cmd.exe","/c","cls"])
		respuesta = "si"
		print("eres mayor a 10? ")
		if edad > 10:
			respuesta = "no"
		print("{}, tengo {}".format(respuesta, edad))
		if edad > 10:
			print("no puedes pasar")
		else:
			print("puedes pasar")
		timelist.append(cooldown)
		agelist.append(edad)
		edadtotal = promedio(agelist)
		tiempototal = promedio(timelist)
		print("el siguiente va llegar en {} segundos y va a tener {} años".format(tiempototal, edadtotal))
