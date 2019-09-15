import itertools
mylist = ["one","two","tres", "four"]
cycle = 0
for item in itertools.cycle(mylist):
	print(item)
	if item == mylist[-1]:
		cycle += 1
	if cycle == 4:
		break
del mylist
del cycle