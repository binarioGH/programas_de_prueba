#-*-coding: utf-8-*-
from sys import argv

class Lector():
	def __init__(self, f):
		self.chars = {}
		try:
			file = open(f, "r")
			self.content = file.readlines()
		except Exception as e:
			print(e)
			exit()
		else:
			file.close()
			self.readfile()
			self.showstats()

	def readfile(self):
		for line in self.content:
			for char in line.strip():
				if char == " ":
					continue
				else:
					if char in self.chars:
						self.chars[char] += 1
					else:
						self.chars[char] = 1
	def showstats(self):
		for c in self.chars:
			print("{} {} {}%".format(c, self.chars[c],round(100 * self.chars[c] / len(self.chars),2)))

if __name__ == '__main__':
	main = Lector(argv[1])