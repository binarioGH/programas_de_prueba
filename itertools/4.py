#-*-coding: utf-8-*-
from itertools import accumulate
abcsum = lambda a,b:  a+b
data = accumulate(["a","b","c","d","e"], abcsum)
for item in data:
	print(item)