#-*-coding: utf-8-*-
from socket import *
from os import chdir, getcwd

if __name__ == "__main__":
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(("127.0.0.1", 5000))
	sock.listen(1)
	conn, addr = sock.accept()
	while True:
		cmd = conn.recv(1024).decode()
		if cmd[:2] == "cd":
			try:
				chdir(cmd[3:])
			except:
				conn.send("No se ha encontrado el directorio.".ecnode())
			finally:
				conn.send(getcwd().encode())
		else:
			try:
				conn.send("Se ha empezado una descarga. {}".format(cmd).encode())
				file = open(cmd, "rb")
				for line in file.read(1024):
					conn.send(line)
				conn.send("Se ha terminado la descarga.".encode())
			except Exception as e:
				conn.send("Ha habido un problema al abrir el archivo. \n{}".format(e).encode())


