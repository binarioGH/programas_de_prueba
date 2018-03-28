#-*- coding: utf-8 -*-
# 8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro 
# en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado. 
import random
def superposicion(list1, list2):
	same = False
	for num1 in list1:
		for num2 in list2:
			if num1 == num2:
				same = True
	return same
if __name__ == '__main__':
    count = 0
    flist = []
    slist = []
    while count < 3:
		ran1 = random.randint(1,3)
		flist.append(ran1)
		ran2 = random.randint(1,3)
		slist.append(ran2)
		count += 1
    comp = superposicion(flist, slist)
    if comp == True:
		print("tienen numeros en comun")
    else:
		print("no hay numeros en comun")