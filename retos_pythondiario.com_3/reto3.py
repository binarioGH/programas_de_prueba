#-*-coding: utf-8-*-
# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene 
# que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
if __name__ == '__main__':
	word1 = str(raw_input("introduce una palabra: "))
	word2 = str(raw_input("introduce otra palabra: "))
	if len(word1) < 2 or len(word2) < 2:
		print("ocupas palabras más largas para rimar")
	if word1[len(word1) -4::] == word2[len(word2) -4::] and word1 != word2: 
		print("riman")
	elif word1 == word2:
		print("las palabras iguales no riman")
	elif word1[len(word1) -3 ::] == word2[len(word2) -3 ::] and word1[len(word1) -4] != word2[len(word2) -4] and word1 != word2:
		print("riman un poco")