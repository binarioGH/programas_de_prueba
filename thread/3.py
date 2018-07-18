#-*-coding: utf-8 -*-
from threading import *
import time

def saludar(n1, n2):
	print("Hola {}".format(n1))
	time.sleep(2)
	print("Hola {}".format(n2))


if __name__ == '__main__':
	hilo = Thread(target=saludar, args=("carlos", "codigo"))#args se usa cuando la función que se va a ejecutar
	#requiere argumentos.
	hilo.start()
	print("Si esto se imprime el codigo funciona.")