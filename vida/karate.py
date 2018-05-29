#-*-coding: utf-8 -*-
import random
from time import sleep
# Estaba en clase de karate senpai (maestro/a) me pidió que diera la clase mientras ella atendía sus clientes.
# No se me ocurría que poner, así que pensé en preguntarle a cada estudiante y si es que se tardaban en
# hablar todos haríamos 10 sentadillas, lagartijas o abdominales, por eso pensé en hacer este algoritmo.
if __name__ == '__main__':
	estudiantes = ("Carlos","Enrique","Diego","Sofia","Juan","Luis")
	castigos = ("abdominales","sentadillas", "lagartijas")
	ejercicios = ("patadas", "golpes", "defensas")
	for estudiante in estudiantes:
		print("{} pon un ejercicio.".format(estudiante))
		tiempo = random.randint(0, 5)
		sleep(tiempo)
		if tiempo > 2:
			print("te tardaste, hagan {} {}".format(random.randint(5, 10), random.choice(castigos)))
		else:
			print("{}: {}".format(estudiante, random.choice(ejercicios)))