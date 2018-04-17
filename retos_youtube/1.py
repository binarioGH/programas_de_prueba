#-*-coding: utf-8-*-
# https://www.youtube.com/watch?v=7WMSLasIuXo
# python 3

if __name__ == '__main__':
	word = input("introduzca una palabra: ")
	block = input("introduzca una letra que le quiera quitar: ")
	if len(block) != 1:
		print("solo una letra")
		exit()
	for letter in word:
		if letter == block:
			continue
		print(letter)

	