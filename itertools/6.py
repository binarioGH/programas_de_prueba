#-*-coding: utf-8-*-
from itertools import compress
def boolList(l):
	blist = []
	for i in l:
		if type(i) == type(""):
			blist.append(False)
		else:
			blist.append(True)
	return blist
l1 = ["1",2,3,4,5,"6"]
l2 = boolList(l1)
compressedList = compress(l1,l2)
for i in compressedList:
	print(i)