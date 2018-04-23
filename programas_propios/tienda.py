#-*-coding: utf-8-*-
import subprocess
price = {1: 20, 2: 10, 3: 500, 4 : 100, 5: 150}
if __name__ == '__main__':
	money = 1000
	while money > 0:
		subprocess.call(["cmd.exe","/c","cls"])
		buy = int(input('''
dinero: {}
		1	galletas : 20
		2	jugo : 10
		3	computadora : 500
		4	cama : 100
		5       teclado : 150

introduzca el numero del producto que desea comprar: '''.format(money)))
		try:
			if money >= price[buy]:
				money -= price[buy]
			else:
				print("no le alcanza para eso")
				subprocess.call(["cmd.exe","/c", "pause"])
		except:
			print("esa no es una opcion valida")
			subprocess.call(["cmd.exe","/c","pause"])
