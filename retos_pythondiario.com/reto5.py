#-*- coding: utf-8 -*-
# 5- Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los 
# números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
def suml(numlist):
	total = 0
	for num in numlist:
		total += num
	print(total)

def multl(numlist):
	total = 1
	for num in numlist:
		total *= num
	print(total)
if __name__ == '__main__':
	listnum = []
	wt = True
	while wt:
		try:
			add = int(raw_input("introduce un numero: "))
			listnum.append(add)
		except Exception as e:
			print("ese no es un numero entero")
		fin = str(raw_input("'p' para parar, de lo contrario introduzca cualquier cosa: "))
		if fin == "p":
			decide = str(raw_input("'s' para sumar y 'm' para multiplicar: "))
			if decide == 's':
				suml(listnum)
				wt = False
			else:
				multl(listnum)
				wt = False





