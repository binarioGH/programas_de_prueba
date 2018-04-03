#-*- coding: utf-8 -*-
# Escribe un programa que te permita jugar a una versión simplificada del juego Master 
# Mind. El juego consistirá en adivinar una cadena de números distintos. Al principio, el 
# programa debe pedir la longitud de la cadena (de 2 a 9 cifras). Después el programa debe ir 
# pidiendo que intentes adivinar la cadena de números. En cada intento, el programa informará de cuántos 
# números han sido acertados (el programa considerará que se ha acertado un número si coincide el valor y
# la posición).
# Dime la longitud de la cadena: 4
# Intenta adivinar la cadena: 1234
# Con 1234 has adivinado 1 valores. Intenta adivinar la cadena: 1243
# Con 1243 has adivinado 0 valores. Intenta adivinar la cadena: 1432
# Con 1432 has adivinado 2 valores. Intenta adivinar la cadena: 2431
# Con 2431 has adivinado 4 valores. Felicidades
import random
def cadena(lng):
	num = str()
	for i in range(0, lng):
		num += str(random.randint(0,9))
    	return num
if __name__ == '__main__':
	try:
		lng = int(raw_input("introduzca la longitud de la cadena: "))
	except Exception as e:
		print("valor invalido")
		exit()
	else: 
		cadena = cadena(lng)
		string = str()
		while string != cadena:
			try: 
				count = 0
				points = 0
				string = str(raw_input("introduce la cadena: "))
				for i in string:
					if i == cadena[count]:
						points += 1
						count += 1
				print("con {} has acertado {} digitos".format(string, points))
			except Exception as e:
				print("error")
		print("ganaste")

