#-*-coding: utf-8-*-
import threading
import time

class Mihilo(threading.Thread):
	def run(self):
		print("{} inició.".format(self.getName()))
		time.sleep(5)
		print("{} terminado.".format(self.getName()))
if __name__ == '__main__':
	for x in range(4):
		hilo = Mihilo(name="Thread-{}".format(x+1))
		hilo.start()
		time.sleep(.5)