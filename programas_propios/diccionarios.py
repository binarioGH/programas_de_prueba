#-*-coding: utf-8-*-
from sys import argv
if __name__ == '__main__':
	count = 0
	lst = []
	possiblepassword = []
	for arg in argv:
		if arg == "-i":
			for a in argv[count + 1:]:
				lst.append(a)
				count += 1
		else:
			count += 1
	for data in lst:
		for i in lst:
			pss = data + i
			possiblepassword.append(pss)
	for pp in possiblepassword:
		print(pp)