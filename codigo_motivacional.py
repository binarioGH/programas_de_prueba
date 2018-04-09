#-*- coding: utf-8-*-
import time
import subprocess
# este programa es una idea que salío de un vídeo: https://www.youtube.com/watch?v=1eMO7FIR4_o
while True:
	for h in range(0, 24):
		for m in range(0,  60):
			for s in range(0, 60):
				subprocess.call(["cmd.exe","/c","cls"])
				print("horas: {}, minutos: {}, segundos: {}".format(h,m,s))
				time.sleep(1)
				if h == "nunca" or m == "nunca" or s == "nunca":
					print("es demasiado tarde :( ")
					exit()