#-*-coding: utf-8-*-
from sys import argv
import subprocess

if __name__ == '__main__':
	for i in range(10):
		subprocess.call(["cmd.exe","/c","mkdir {}".format(i)])
		subprocess.call(["cmd.exe", "/c", "copy {} {}".format(argv[0], i)])