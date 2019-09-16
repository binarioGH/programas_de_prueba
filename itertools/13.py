#-*-coding: utf-8-*-
from itertools import combinations

letters = ["a","b","c","d","e","f","g","h"]
combined = combinations(letters, 2)
for combination in combined:
	print(combination)