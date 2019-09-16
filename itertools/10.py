#-*-coding: utf-8-*-
from itertools import starmap 

sumabc = lambda a,b: a+b

data = [("a", "b"), ("c", "d"), ("e", "f")]

iterator = starmap(sumabc, data)
for i in iterator: 
	print(i)