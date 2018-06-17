#-*-coding: utf-8-*-
import socket
if __name__ == '__main__':
	host = "127.0.0.1"
	port = 5000
	client = socket.socket()
	client.connect((host, port))
	while True:
		mensaje = input("Manda un mensaje: ")
		client.send(mensaje.encode())
		datos = client.recv(2080).decode()
		print("Respuesta: {}".format(datos))
