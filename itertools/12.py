#-*-coding: utf-8-*-
from itertools import zip_longest
letters = ("a","b","c","d","e","f","g")
numbers = range(1,24)
together = zip_longest(numbers, letters, fillvalue="Oops!")
for i in together:
	print(i)