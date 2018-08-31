#-*-coding: utf-8-*-
#https://recursospython.com/guias-y-manuales/capturar-pantalla/
from pyautogui import screenshot

if __name__ == '__main__':
 	ss = screenshot() 
 	ss.save("1.jpg")
 	ss.show()	