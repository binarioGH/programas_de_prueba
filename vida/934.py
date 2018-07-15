#-*-coding: utf-8-*-
from sys import argv
#Estaba en un camion con el numero 934, empecé a dividirlo hasta ver con que numeros daba % == 0.
if __name__ == '__main__':
	mx = int(argv[1])
	for num in range(2, int(mx/ 2 + 1)):
		if mx % num == 0:
			print("Es divisible entre {}: {}".format(num, int(mx/num)))