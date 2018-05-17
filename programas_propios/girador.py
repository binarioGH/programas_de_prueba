#-*-coding: utf-8-*-
import subprocess
import time
if __name__ == '__main__':
	count = 0
	symbol = ('|', '/', '-', '\\')
	while True:
		subprocess.call(["cmd.exe","/c","cls"])
		if count == 3:
			count = 0
		print("    {}     {}     {}".format(symbol[count], symbol[count], symbol[count]))
		time.sleep(1)
		count += 1