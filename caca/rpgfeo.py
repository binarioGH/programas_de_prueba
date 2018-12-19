#-*-coding: utf-8-*-
from threading import Thread
from time import sleep
from platform import python_version as pv
from random import randint, choice
class Personaje():
	def __init__(self, nombre, genero):
		self.nombre = nombre
		self.genero = genero
		if self.genero == "h":
			self.letra = ("o", "ó")
		else:
			self.letra = ("a", "á")
		self.comentarios()
		self.status = {"Salud":10,"Hambre": 10, "Fuerza": 3, "Resistencia": 30, "Arma equipada": 0, "Armadura":0}
		self.inventario = {"Poción de resistencia":[1,("Resistencia (debil)", "Resistencia"),5],"Cordero":[3,("Comida", "Hambre"),5]}
		hambruna = Thread(target=self.hunger)
		hambruna.daemon = True
		hambruna.start()
	def comentarios(self):
		self.no_encontrar = ("{}(pensamiento): Quizá me falla la memoría, pero estaba segur{} de que dejé eso aquí".format(self.nombre, self.letra[1]),"{}(Pensamiento): Juraría que tenía un poco aún".format(self.nombre),"{}(Pensamiento): Diablos, ya no tengo más".format(self.nombre),"{}(pensamiento): ¿Donde quedó eso que estoy buscando?".format(self.nombre))
		self.acabar=("{}(pensamiento): Creo que ese era el ultimo...".format(self.nombre),"{}(pensamineto): Y ahí va la ultima que quedaba...".format(self.nombre),"{}(pensamiento): Creo que con eso no quedan más.".format(self.nombre))
	def hunger(self):
		while True:
			sleep(self.status["Resistencia"])
			if self.status["Hambre"] <= 0:
				self.status["Salud"] -= 1
				if self.status["Salud"] == 5:
					print("{}(pensamiento): Estoy en un muy mal estado".format(self.nombre))
			else:
				self.status["Hambre"] -= 1
				if self.status["Hambre"] == 5:
					print("{}(pensamiento): Empiezo a sentir hambruna".format(self.nombre))
	def verInventario(self):
		print("Objeto      |      Cantidad       |      Tipo")
		for item in self.inventario:
			print("----------------------------------------")
			print("{}      |      {}      |      {}".format(item,self.inventario[item][0],self.inventario[item][1][0]))
	def verStatus(self):
		for necesidad in self.status:
			print("{}: {}".format(necesidad, self.status[necesidad]))
	def consumir(self, item):
		if item in self.inventario:
			self.status[self.inventario[item][1][1]] += self.inventario[item][2]
			self.inventario[item][0] -= 1
			if self.inventario[item][0] <= 0:
			    del self.inventario[item]
			    print(choice(self.acabar))		
		else:
			print(choice(self.no_encontrar))

if __name__ == '__main__':
	if str(pv())[0] == "3":
		raw_input = input
	n = str(raw_input("Ingresa el nombre de tu personaje: "))
	g = ""
	while g != "h" and g != "m":
		g = str(raw_input("Ingresa el genero de tu personaje [h / m]: "))
	mc = Personaje(n, g)
	cmd = ""
	while cmd != "gameover":
		try:
			cmd = raw_input("({})--|>>>>".format(mc.nombre))
			if cmd == "inventario":
				mc.verInventario()
			elif cmd == "status":
				mc.verStatus()
			elif cmd[:4] == "usar":
				mc.consumir(cmd[5:])
		except IndexError:
			pass
		except Exception as e:
			print("ERROR: {}".format(e))