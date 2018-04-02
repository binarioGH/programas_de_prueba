#-*- coding: utf-8 -*-
# Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.7
# Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
if __name__ == '__main__':
	try:
		year = int(raw_input("introduce un año: "))
	except Exception as e:
		print("ese no es un año")
		exit()
	if year % 4 == 0:
		print("es bisiesto")
	else:
		print("no es bisiesto")