#-*-coding: utf-8-*-
import random


def suma(lst):
	rslt = []
	olst = []
	for num in lst:
		total = 0
		olst.append(num)
		for num2 in olst:
			total += num2
		rslt.append(total)
	return rslt

if __name__ == '__main__':
	lista = []
	while len(lista) < random.randint(3, 5):
		lista.append(random.randint(1, 10))
	ttl = suma(lista)
	print("{}\n\n\n{}".format(lista, ttl))
	


		
