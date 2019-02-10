#-*-coding: utf-8-*-
matrizA = ((1,2,3,4),(5,6,7,8))
matrizB = ((5,5,3,1),(5,1,6,4))
matrizC = [[],[]]
fila = 0
columna = 0
while len(matrizC[1]) != len(matrizA[0]):
	matrizC[fila].append(matrizA[fila][columna] + matrizB[fila][columna])
	columna += 1
	if columna == len(matrizA[0]):
		fila += 1
		columna = 0

print("La suma es:\n{}".format(matrizC))