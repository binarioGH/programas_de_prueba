#-*-coding: utf-8-*-
# Escribir un pequeño programa donde:
# - Se ingresa el año en curso.
# - Se ingresa el nombre y el año de nacimiento de tres personas.
# - Se calcula cuántos años cumplirán durante el año en curso.
# - Se imprime en pantalla.
if __name__ == '__main__':
	try:
		actual = int(raw_input("introduce el año actual: "))
	except Exception as e:
		print("ese no es un año")
		exit()
	personas = {}
	wt = True
	count = 0

	while wt:
		p = str(raw_input("ingresa un nombre: "))
		try:
			personas[p] = int(raw_input("en que año nació {}?: ".format(p)))
		except Exception as e:
			print("ese no es un año")
			exit()
		count += 1
		if count >= 3:
			wt = False 
	for i in personas:
		print("{} va a cumplir {} en este {}".format(i,actual - personas[i], actual))


	