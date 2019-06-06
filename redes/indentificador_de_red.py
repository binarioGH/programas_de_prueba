#-*-coding: utf-8-*-
from sys import argv

def identifynet(ip):
	try:
		octets = ip.split(".")
		idclass = int(octets[0])
	except:
		return "Fail"
	if idclass >= 0 and idclass <= 127:
		return "A"
	elif idclass >= 128 and idclass <= 191:
		return "B"
	elif idclass >= 192 and idclass <= 223:
		return "C"
	elif idclass >= 224 and idclass <= 239:
		return "D"
	elif idclass >= 240 and idclass <= 255:
		return "E"
	else:
		return "Fail"


def main():
	if len(argv) != 2:
		print("Incorrect arguments.")
		print("Usage: [program] [ip]")
		exit()
	ip = argv[1]
	ipclass = identifynet(ip)
	if ipclass == "Fail":
		print("{} is not a valid ip.".format(ip))
		exit()
	print("{} is an ip class {}".format(ip ,ipclass));

if __name__ == '__main__':
	main()