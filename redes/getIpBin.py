#-*-coding: utf-8-*-
from n2b import getBin as binary
from sys import argv

def getIpBinary(ip):
	octetes = ip.split(".")
	binip = []
	for octete in octetes:
		b = binary(int(octete))
		binip.append(b)
	return ".".join(binip)

def main():
	print("{}".format(getIpBinary(argv[1])))

if __name__ == '__main__':
	main()