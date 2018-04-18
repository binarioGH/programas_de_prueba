#-*-coding: utf-8-*-
# https://www.youtube.com/watch?v=7WMSLasIuXo
# python 3

import random

if __name__ == '__main__':
	numlist = [0]
	while len(numlist) < 10:
		numlist.append(random.randint(-5, 5))
	zerocount = 0
	for num in numlist:
		if num == 0:
			zerocount += 1
			continue
		elif num < 0:
			print("{} es negativo".format(num))
		else:
			print("{} es positivo".format(num))
	c = "cero"
	if zerocount > 1:
		c = "ceros"

	print("habia: {} {} en la lista".format(zerocount, c))


