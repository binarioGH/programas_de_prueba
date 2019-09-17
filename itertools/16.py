#-*-coding: utf-8-*-
#this will allow me to make a dictionary generator.
from itertools import permutations
data1 = ["1","2","3","4","5"]
result = permutations(data1)
for data in result:
	print("".join(data))