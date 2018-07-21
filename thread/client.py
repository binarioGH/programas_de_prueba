#-*-coding: utf-8-*-
#https://www.youtube.com/watch?v=-eT0-w9SipA
from socket import *
import threading

def recv():
	while True:
		rcv = sock.recv(1024).decode()
		rcv += "\n"
		print(rcv)

if __name__ == '__main__':
	msg = str()
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect(("127.0.0.1", 5000))
	thread = threading.Thread(target=recv)
	thread.daemon = True
	thread.start()
	print("Ingresa un mensaje para el servidor o ingresa 'salir' para terminar.")
	while msg != "salir":
		
		msg = input(">")
		sock.send(msg.encode())
	sock.close()