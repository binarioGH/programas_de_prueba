#-*-coding: utf-8 -*-
# 10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima 
# un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******
import random
def procedimiento(numlist, char):
	for num in numlist:
		histograma = char * num
		print(histograma)
if __name__ == '__main__':
    charlist = ["x","*","+"]
    ranchar = random.choice(charlist)
    listdenum = [4, 9, 7]
    procedimiento(listdenum, ranchar)
	
