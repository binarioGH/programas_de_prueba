#-*- coding: utf-8 -*-
# Diseñar un sistema de puntos para el juego El reino del dragón:
# Dejo el enlace por si alguien no lo vio: http://www.pythondiario.com/2013/06/juego-en-python-reino-del-dragon-parte-1.html
# La idea es la siguiente: mientras el jugador vaya ganando, ira acumulando puntos.
# Ejemplo: Si el jugador entra en la primera cueva y gana el tesoro, se le acreditan 100 puntos, entra en 
# la segunda cueva y gana el tesoro, se le acreditan otros 100 puntos. Si el jugador pierde, saldrá en pantalla el 
# total de los puntos que realizo y la opción de empezar de nuevo.
import time
import random
import subprocess
if __name__ == '__main__':
	wt = True
	point = 0
	while wt:
		subprocess.call(["cmd.exe","/c","cls"])
		print("puntos: {}".format(point))
		print("Estamos en una tierra llena de dragones. Delante de nuestro,")
		print("se ven dos cuevas. En una cueva, el dragon es amigable")
		print("y compartira el tesoro contigo. El otro dragon")
		print("es codicioso y hambriento, y te va a comer ni bien te vea.")
		print("")
		time.sleep(3)
		luck = random.randint(1, 2)
		if luck == 1:
			print("el dragon es malo y te come")
			point -= 1
		elif luck == 2:
			print("el dragon es bueno y te da un tesoro")
			point += 1
		re = str(raw_input("quiere volver a jugar? y/n: "))
		if re == "n" or re == "N":
			wt = False
			







