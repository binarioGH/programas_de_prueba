#-*-coding: utf-8 -*-
# Escribir una función filtrar_palabras() que tome una lista de palabras 
# y un entero n, y devuelva las palabras que tengan mas de n caracteres. 
import random
def filtro(slist, maxnum):
	p_filtradas = []
	for word in slist:
		wordsize = len(word)
		if wordsize > maxnum:
			p_filtradas.append(word)
	print("las palabras con mas de {} letras son: ".format(maxnum))
	for filt in p_filtradas:
		print(filt)
if __name__ == '__main__':
	count = 0
	strlist = []
	nmax = random.randint(5, 8)
	while count <= 4:
		ystr = str(raw_input("introduzca un string: "))
		strlist.append(ystr)
		count += 1
	filtro(strlist, nmax)

