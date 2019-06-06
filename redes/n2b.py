#-*-coding: utf-8-*-

def getBin(num):
	if num > 255:
		return False
	else:
		bits = (128,64,32,16,8,4,2)
		byte = ""
		for n in bits:
			if n >= num:
				num -= n
				byte += "1"
			else:
				byte += "0"
    return byte