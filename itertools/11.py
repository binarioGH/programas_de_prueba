#-*-coding: utf-8-*-
from itertools import tee
def printout(iter):
	for i in iter:
		print(i)
lst = [1,2,3,4,5,6]
l1, l2 = tee(lst)
printout(l1)
printout(l2)