#-*-coding: utf-8-*-
from socket import *
import threading

def recv():
	while True:
		rcv = conn.recv(1024).decode()
		rcv += "\n"
		print(rcv)
if __name__ == '__main__':
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(("127.0.0.1",5000))
	sock.listen(1)
	conn, addr = sock.accept()
	print("Se ha iniciado una conexión: {}".format(addr))
	thread = threading.Thread(target = recv)
	thread.daemon = True
	thread.start()
	msg = str()
	while msg != "salir":
		msg = input(">")
		conn.send(msg.encode())
