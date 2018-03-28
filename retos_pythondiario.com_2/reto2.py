#-*- coding: utf-8 -*-
# Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga. 
def mas_larga(strlist):
    maxstr = 0
    for string in strlist:
    	longstr = len(string)
    	if longstr > maxstr:
    		maxstr = longstr
    		mlong = string
    print("la palabra mas larga es {} y tiene {} letras".format(mlong, maxstr))
if __name__ == '__main__':
	stringl = []
	wt = True
	count = 0
	while count <= 4:
		ystr = str(raw_input("introduzca un string: "))
		stringl.append(ystr)
		count += 1
        
	mas_larga(stringl)
