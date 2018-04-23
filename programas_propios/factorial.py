#-*-coding: utf-8 -*-
if __name__ == '__main__':
	try:
		n = int(input("introduzca un numero: "))
	except:
		print("este programa solo funciona con numeros enteros.")
		exit()
	n += 1
	fac = 1
	for num in range(n):
		if num == 0:
			continue
		else:
			fac *= num
	print("el factorial de {} es {}".format(n -1, fac))



