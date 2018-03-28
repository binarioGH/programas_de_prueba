#-*- coding: utf-8 -*-
# 7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo 
# aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
def palindromo(pal):
	if pal == pal[::-1]:
		print("es palindromo")
	else:
		print("no es palindromo")
if __name__ == '__main__':
	word = str(raw_input("introduce una palabra: "))
	palindromo(word)