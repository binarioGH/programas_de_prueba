#-*-coding:utf-8-*-
import subprocess
import getpass
def cfrar(dic, word):
	count = 4
	sentence = str()
	for letter in word:
		count = 4
		for lt in dic[3:]:
			if letter == lt:
				sentence += dic[count - 4]	
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
		
		[c]ifrar                
	        [exit] para salir... 

	        >'''))
		ask = ask.lower()
		print("\n\n\n")
		if ask == "c":
			palabra = str(input("introduzca la palabra que quiere cifrar: "))
			result = palabra.lower()
			result = cfrar(abc, palabra)
			print("la palabra {} cifrada es: {}".format(palabra, result))
			getpass.getpass("")

			








	
