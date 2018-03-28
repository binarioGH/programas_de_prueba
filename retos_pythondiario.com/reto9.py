#-*-coding: utf-8 -*-
# 9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter
# multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"
def n_caracteres(num, char):
	print(num * char)
if __name__ == '__main__':
	n = str(raw_input("introduzca un caracter: "))
	try:
		rep = int(raw_input("introduzca el numero de veces que se repetira: "))
		n_caracteres(rep, n)
	except Exception as e:
		print("ese no es un numero entero")
	