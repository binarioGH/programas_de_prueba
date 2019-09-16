#-*-coding: utf-8-*-
from itertools import dropwhile
def drop(n):
	return n < 5

data = [1,2,4,5,6,6,7,8,9,10]
surviving = dropwhile(drop, data)
for i in surviving:
	print(i)

