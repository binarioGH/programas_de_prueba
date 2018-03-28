#-*-coding: utf-8 -*-
# 1- Definir una función max() que tome como argumento dos números 
# y devuelva el mayor de ellos. (Es cierto que python tiene una función max()
# incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

# la funcion se llama "rmax" por "reto max"
def rmax(num1, num2):
	if num1 > num2:
		print("{} es mayor que {}".format(num1, num2))
	elif num1 == num2:
		print("son iguales")
	else:
		print("{} es mayor que {}".format(num2, num1))


if __name__ == '__main__':
	print("ingresa solo numeros enteros")
	try:
		number1 = int(raw_input("ingresa un numero: "))
		number2 = int(raw_input("ingresa otro numero: "))
		rmax(number1, number2)
	except Exception as e:
		print("ese no es un numero entero")
		
