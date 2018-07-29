#-*-coding: utf-8 -*-
import threading
from time import sleep

class Main:
	def __init__(self):
		self.lista = [1,2,3,4,5]
		hilo = threading.Thread(target=self.apnd)
		hilo.daemon = True
		hilo.start()
		for i in self.lista:
			sleep(1)
			print(i)
	def apnd(self):
		for i in range(6, 11):
			self.lista.append(i)
if __name__ == '__main__':
	start = Main()
	