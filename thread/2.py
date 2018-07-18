#-*-coding: utf-8 -*-
import threading

def hm():
	print("Hola mundo.")
if __name__ == '__main__':
	hilo = threading.Thread(target=hm())#target sirve para ejecutar codigo en segundo plano
	hilo.start()

