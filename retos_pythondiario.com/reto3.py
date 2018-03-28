#-*- coding: utf-8 -*-
# 3- Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python 
# tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.)

#sol se refiere a "string or list"
def rlen(sol):
    # sorl significa "string or list"
	count = 0
	for sorl in sol:
		count += 1
	print(count)
if __name__ == '__main__':
	decide = str(raw_input("'s' para string y 'l' para lista: "))
	if decide == "s":
		try:
			thestr = str(raw_input("ingresa tu string: "))
			rlen(thestr)
		except Exception as e:
			print("ese no es un string")
	elif decide == "l":
		thelist = []
		wt = True
		while wt:
			add = str(raw_input("ingresa un string: "))
			thelist.append(add)
			finish = str(raw_input("para continuar agregando elementos a la lista use 's' y para parar 'p': "))
			if finish == "p":
				rlen(thelist)
				wt = False

				
