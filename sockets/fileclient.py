#-*-coding: utf-8-*-
from socket import *
from threading import *
from time import strftime
def receiving():
	while True:
		try:
			r = sock.recv(1024).decode()
			print(r)
			try:
				if r[:28] == "Se ha empezado una descarga.":
					file = open(r[29:], "wb")
					while True:
						r = sock.recv(1024)
						if r.decode() == "Se ha terminado la descarga." or r[:42].decode() == "Ha habido un problema al abrir el archivo.":
							print("Descarga terminada o interrumpida.\n{}".format(r.decode()))
							file.close()
							break
						file.write(r)
			except:
				pass				

		except:
			pass

if __name__ == '__main__':
	sock = socket(AF_INET)
	sock.connect(("127.0.0.1", 5000))
	snd = str()
	r = Thread(target=receiving)
	r.daemon = True
	r.start()
	while snd != "exit":
		snd = input(">>>")
		sock.send(snd.encode())
