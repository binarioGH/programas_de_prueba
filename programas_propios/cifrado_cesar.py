#-*-coding:utf-8-*-
import subprocess
import getpass
def cfrar(dic, word, num, minim, maxim, cnt):
	count = cnt
	sentence = str()
	for letter in word:
		count = cnt
		for lt in dic[minim:maxim]:
			if letter == lt:
				sentence += dic[count + num]
			else:
				if letter == " ":
					sentence += " " 
					break
				elif letter == ".":
					sentence += "."
					break
				elif letter == ",":
				    sentence += ","
				    break 
			count += 1
	return sentence
if __name__ == '__main__':
	abc = ("x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z")
	ask = str()
	while ask != "exit":
		subprocess.call(["cmd.exe","/c","cls"])
		ask = str(input('''
		----C I F R A D O----
		   ---C E S A R---    
		
		[d]ecifrar
		[c]ifrar                
	        [exit] para salir... 
	    

	        >'''))
		ask = ask.lower()
		print("\n\n\n")
		if ask == "c":
			palabra = str(input("introduzca la frase o palabra que quiere cifrar: "))
			palabra = palabra.lower()
			result = cfrar(abc, palabra, -4, 3, 28, 4)
			print("la frase o palabra {} cifrada es: {}".format(palabra, result))
			getpass.getpass("")
		elif ask == "d":
			palabra = str(input("introduzca la frase o palabra que quiere descifrar: "))
			palabra = palabra.lower()
			result = cfrar(abc, palabra, 4, 0, 24, -1)
			print("la frase o palabra {} descifrada es: {}".format(palabra, result))
			getpass.getpass("")