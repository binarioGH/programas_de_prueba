#-*-coding: utf-8-*-
# este programa es creado debido a que leyendo sobre redes vi que la formula
# para ver cuantos cables ocupas en tu red malla es n * n -1 / 2

if __name__ == '__main__':
	n = int(input("cuantas computadoras hay en tu red malla? "))
	n *= n - 1
	n /= 2
	print("ocupas {} cables".format(n))