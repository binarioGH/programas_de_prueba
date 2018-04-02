#-*- coding: utf-8-*-
# Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
# También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
if __name__ == '__main__':
	names = ["andrea", "tomas", "Ruben", "Antonio", "Jose", "joel", "javier", "carlos", "ivana"]
	char = str(raw_input("introduce el caracter que quieres buscar: "))
	if len(char) > 1:
		print("solo 1 caracter")
		exit()
	count = 0
	# schar significa search char
	for schar in names:
		if schar[0] == char.lower() or schar[0] == char.upper():
			count += 1
	print("hay {} personas que empiezan con {} en esta lista".format(count, char))
	

