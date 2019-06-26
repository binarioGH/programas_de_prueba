#-*-coding: utf-8-*-
from os import listdir, chdir, system

def change(d, k):
	try:
		chdir(d)
	except Exception as e:
		print(e)
	else:
		kin = len(k)
		toclean = [file for file in listdir(d) if file[:kin] == k]
		counter = 0
		for file in toclean:
			newfile = file[kin:] 
			system("move {} {}".format(file, newfile))
			print("{} files moved so far.".format(counter))
			counter += 1
def main():
	dir = input("Input the path: ")
	key = input("Input the key: ")
	change(dir, key)


if __name__ == '__main__':
	main()