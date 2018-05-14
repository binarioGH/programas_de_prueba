#-*-coding: utf-8-*-
#https://www.youtube.com/watch?v=2Cc1ZUD2v8s
import random
import time
import subprocess
class Carro:
	def __init__(self, marca, color):
		self.marca = marca
		self.color = color
	def acelerar(self):
		print("acelerando")
	def frenar(self):
		print("frenando")
	


if __name__ == '__main__':
	colores = ("rojo", "verde", "negro", "blanco")
	marcas = ("nissan", "ferrari", "toyota") #no conozco más marcas de carros
	tu_carro = Carro(random.choice(marcas), random.choice(colores))
	subprocess.call(["cmd.exe", "/c", "cls"])
	print('''
		vas en tu carro de marca {} y de color {}'''.format(tu_carro.marca, tu_carro.color))
	time.sleep(2)
	chose = input('''
		de la nada aparece un trailer y tu tienes que decidir
		si [f]renar o [a]celerar
		
		>''')
	time.sleep(1)
	if chose == "f":
		tu_carro.frenar()
	else:
		tu_carro.acelerar()
	if random.randint(0, 1) == 1:
		print("tu carro choca y mueres")
	else:
		print("te salvaste")
		
		
