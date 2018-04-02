#-*- coding: utf-8 -*-
# Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20.
# Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
import random
if __name__ == '__main__':
	count = 0
	# lo hice con una lista y no con una tupla porque a las tuplas no se les puede agregar nada.
	edades = []
	while count <= 10:
		edades.append(random.randint(0,50))
		count += 1
	count2 = 0
	for age in edades:
		if age > 20:
			count2 += 1
	print("hay {} personas mayores a 20 en esta lista".format(count2))
	print(edades)
