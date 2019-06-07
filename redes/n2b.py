#-*-coding: utf-8-*-
def getBin(num):
	if num > 255:
	    return False

	else:
		binary = [""] * 8
		for bit in range(len(binary)):
			binary[bit] = str(num % 2)
			num = int(num / 2)
	binary = "".join(binary)
	binary = binary[::-1]
	return binary

