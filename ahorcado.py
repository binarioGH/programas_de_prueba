#-*- coding: utf-8-*-
import random
import subprocess

hanged_man = ('''
	_________
    |         |
    |        
    |        
    |        
    |
    |''','''
	_________
    |         |
    |         0
    |        
    |        
    |
    |

	''','''
	_________
    |         |
    |         0
    |        /|\
    |        
    |
    |
	''','''
	_________
    |         |
    |         0
    |        /|\
    |        / \
    |_''')
words = ("hola", "mundo", "rojo", "negro", "casa", "caza", "papel", "ola", "torre", "internet", "programar")
if __name__ == '__main__':
	count = 0
	guess = True
	gsscount = 0
	errcount = 0
	while count < len(hanged_man) - 1:

		if guess == True:
			word = random.choice(words)
			guess = False
			wrd = "{-}" * len(word)
		else: 
			subprocess.call(["cmd.exe", "/c", "cls"])
			answ = input('''
				{}
                {}
                {}
                introduzca una palabra:> '''.format(hanged_man[count], wrd, "{} letras adivinadas".format(gsscount)))
			if answ == word:
				subprocess.call(["cmd.exe", "/c", "cls"])
				print("Bien, ganaste")
				guess = True
				subprocess.call(["cmd.exe", "/c", "pause"])
			else:
				for letter in answ:
					for l in word:
						if l == letter:
							gsscount += 1
						else: 
							errcount += 1
				if errcount >= len(word):
					errcount = 0
					count += 1