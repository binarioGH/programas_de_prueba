#-*-coding: utf-8-*-

def esvocal(letra):
	vocales = ("a","e","i","o","u")
	if letra.lower() in vocales:
		return True
	return False

def main():
	l = input("Dame una letra >")
	if(esvocal(l)):
		print("Es vocal")
	else:
		print("No es vocal")

if __name__ == '__main__':
	main()