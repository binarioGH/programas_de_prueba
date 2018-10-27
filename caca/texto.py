#-*-coding: utf-8-*-
#http://www.pythondiario.com/2018/10/analizador-de-texto-programas-python.html
from sys import argv
class Main():
	def __init__(self):
		try:
			with open(argv[1]) as file:
				self.content = file.readlines()
		except Exception as e:
			print(e)
			exit()
	def count(self):
		self.letters = {"numeros": 0,"otros":0,"a": 0,"b": 0,"c": 0,"d": 0,"e": 0,"f": 0,"g": 0,"h": 0,"i": 0,"j": 0,"k": 0,"l": 0,"m": 0,"n": 0,"ñ": 0,"o": 0,"p": 0,"q": 0,"r": 0,"s": 0,"t": 0,"u": 0,"v": 0,"w": 0,"x": 0,"y": 0, "z": 0}
		for line in self.content:
			for char in line:
				if char.lower() in self.letters:
					self.letters[char.lower()] += 1
				else:
					try:
						char = int(char)
					except:
						self.letters["otros"] += 1
					else:
						self.letters["numeros"] += 1
	def porcent(self):
		for t in self.letters:
			if self.letters[t] != 0:
				print("{} : {}".format(t,self.letters[t]))


if __name__ == '__main__':
	start = Main()
	start.count()
	start.porcent()
