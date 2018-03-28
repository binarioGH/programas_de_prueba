#-*-coding: utf-8-*-
# 6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo 
# la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
def inversa(palabra):
	print(palabra[::-1])
if __name__ == '__main__':
	word = str(raw_input("introduce un string: "))
	inversa(word)