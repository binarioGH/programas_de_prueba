#-*-coding: utf-8-*-
import socket 

if __name__ == '__main__':
	host = "127.0.0.1"
	port = 5000
	mySocket = socket.socket()
	mySocket.connect((host, port))
	mensaje = str()
	while mensaje != "q":
		mensaje = str(input("introduzca mensaje: "))
		mySocket.send(mensaje.encode())
		datos = mySocket.recv(1024).decode()
		print("Recibido desde el servidor: {}".format(datos))
	mySocket.close()
