#-*-coding: utf-8-*-
from itertools import product

n = [1,2,3,4]
a = ["a","b","c","d"]
result = product(n,a)
for data in result: 
	print(data )