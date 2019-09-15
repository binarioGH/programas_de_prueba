import itertools

for num in itertools.count(10,3):
	print(num)
	if num >= 20:
		break
del num