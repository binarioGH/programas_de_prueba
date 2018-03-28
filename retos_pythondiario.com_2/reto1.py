#-*-coding: utf-8-*-
# La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), 
# solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos 
# números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
import random
def maxlist(lista):
	maxnum = 0
	for num in lista:
		if num > maxnum:
			maxnum = num
	print("el numero mas grande es: {}".format(maxnum))
	print(lista)
if __name__ == '__main__':
	numlist = []
	count = 0
	while count <= 10:
		ranum = random.randint(1, 20)
		numlist.append(ranum)
		count += 1
	maxlist(numlist)
