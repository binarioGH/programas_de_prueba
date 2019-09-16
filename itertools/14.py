#-*-coding: utf-8-*-
from itertools import combinations_with_replacement as doubles

letters = ["a","b","c"]
result = doubles(letters, 2)
for i in result:
	print(i)