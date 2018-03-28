#-*- coding: utf-8 -*-
# 2- Definir una función max_de_tres(), que tome 
# tres números como argumentos y devuelva el mayor de ellos. 
def rmax2(numlist):
	# maxn se refiere a "maximum number"
	maxn = 0
	for num in numlist:
		if num > maxn:
			maxn = num
	print("{} es el mas grande".format(maxn))
if __name__ == '__main__':
	numberlist = []
	try:
		print("ingresa solo numeros enteros")
		num1 = int(raw_input("ingresa un numero: "))
		numberlist.append(num1)
		num2 = int(raw_input("ingresa un numero: "))
		numberlist.append(num2)
		num3 = int(raw_input("ingresa un numero: "))
		numberlist.append(num3)
		rmax2(numberlist)
	except Exception as e:
		print("ese no es un numero entero")