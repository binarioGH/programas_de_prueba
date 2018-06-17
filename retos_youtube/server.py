#-*-coding: utf-8-*-
import socket 

if __name__ == '__main__':
	host = "127.0.0.1"
	port = 5000
	mySocket = socket.socket()
	mySocket.bind((host,port))
	mySocket.listen(1)
	conn, addr = mySocket.accept()
	print("Conexion desde: {}".format(addr))
	while True:
		datos = conn.recv(1024).decode()
		if not datos:
			break
		print("Desde usuario conectado: {}".format(datos))
		datos = str(datos.upper())
		print("Enviando: {}".format(datos))
		conn.send(datos.encode())
	server.close()
