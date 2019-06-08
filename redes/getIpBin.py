#-*-coding: utf-8-*-
from n2b import getBin as binary

def getIpBinary(ip):
	octetes = ip.split(".")
	binip = []
	for octete in octetes:
		b = binary(int(octete))
		binip.append(b)
	return ".".join(binip)