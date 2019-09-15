import itertools
var = "spam"
for i in itertools.repeat(var, 5):
	print(i)
del var
del i

lst = [1,2,3,4]
for i in itertools.repeat(lst, 5):
	for b in i:
		print(b)