#-*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=VYXdpjCZojA
import random
if __name__ == '__main__':
	class Humano:
		def __init__(self):
			self.edad = random.randint(15, 30)
			print("soy un nuevo objeto")
		def hablar(self):
			print("hola, tengo {} años".format(self.edad))


	pedro = Humano()
	raul = Humano()
	pedro.hablar()
	raul.hablar()
	