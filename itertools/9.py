#-*-coding: utf-8-*-
from itertools import islice

data = [0,1,2,3,4]

few_data = islice(data,1 ,4)

for d in few_data:
	print(d)