#-*-coding: utf-8-*-
import random
import subprocess
def fin(ls):
	subprocess.call(["cmd.exe", "/c", "cls"])
	fn = int(input("cual era tu numero? "))
	for num in ls:
		if num == fn:
			print("eres un mentiroso, el adivinador menciono ese numero.")
			print(ls)
			break
	exit()
if __name__ == '__main__':
	print("debes de pensar en un numero del 1 al 100")
	subprocess.call(["cmd.exe", "/c", "pause"])
	check = str()
	minim = 1
	maxim = 100
	count = 0
	numeros = []
	while check != "=":
		if count == 10:
			fin(numeros)
		subprocess.call(["cmd.exe", "/c", "cls"])
		num = random.randint(minim, maxim)
		numeros.append(num)
		print("el numero en el que piensas es {}?".format(num))
		check = input('''
			intentos: {}
			[+] si tu numero es mayor a {}
			[-] si tu numero es menor a {}
			[=] si tu numero es {}
			
			>'''.format(count, num, num, num))
		if check == "+":
			minim = num + 1
		elif check == "-":
			maxim = num - 1
		count += 1