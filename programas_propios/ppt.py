#-*-coding: utf-8-*-
import random
import subprocess
import getpass

def check(ia, rival):
	if ia == rival:
		return -1
	else:
		return 1

if __name__ == '__main__':
	count = 0
	choose = int()
	items = ("roca", "papel", "tijeras", "roca")
	while choose != 98:
		subprocess.call(["cmd.exe","/c","cls"])
		try:
			choose = int(input('''
				[1]Roca
				[2]Papel
				[3]Tijera

				puntos: {}

				para salir escribe [100]

				> '''.format(count)))
			
				
			print("\n\n\n\n")
			choose -= 1
		except:
			continue
		else:
			iachoice = random.randint(0, 2)
			if choose == iachoice:
				print("los 2 escojieron: {}".format(items[iachoice]))
				getpass.getpass("Presiona enter para continuar...")
				continue
			else:
				print("ppt escogio: {}".format(items[iachoice]))
				print("tu escogiste: {}".format(items[choose]))
				pnt = check(iachoice, choose + 1)
				count += pnt
				getpass.getpass("Presiona enter para continuar...")
