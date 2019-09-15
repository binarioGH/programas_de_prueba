#-*-coding: utf-8-*-
from itertools import chain

l1 = [1,2,4,5]
l2 = ["a","b","c"]

for item in chain(l1,l2):
	print(item)