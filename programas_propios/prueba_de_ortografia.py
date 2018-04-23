#-*- coding: utf-8 -*-
import random
import subprocess
def corrector(pbien, tup):
	if tup == pbien:
		return 1
	else:
		return -1
mw = ("mucica", "presio", "vanda", "kansiones","yenar","majia","chiko","embidia","cinfonia")
gw = ("musica","precio","banda","canciones", "llenar", "magia", "chico", "envidia", "sinfonia")
count = 0
if __name__ == '__main__':
	wt = True
	while wt:
		subprocess.call(["cmd.exe","/c","cls"])
		randint = random.randint(0, len(mw) - 1)
		print('''corrige: {}
puntos: {}'''.format(mw[randint], count))
		yourw = str(raw_input("> "))
		check = corrector(gw[randint], yourw)
		count += check
		if count >= 5:
			wt = False
			print("ganaste")
		elif count <= -3:
			wt = False
			print("perdiste")

		