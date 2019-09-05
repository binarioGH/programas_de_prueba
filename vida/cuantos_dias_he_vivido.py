#-*-coding: utf-8-*-
from time import strftime 
d = lambda f: int(strftime("{}".format(f)))

def main():
	year = int(input("Input the year you were born: "))
	month = int(input("Input the moth you were born: "))
	day = int(input("Input day you were born: "))
	bday = input("did your birthday already passed this year? [y/n]: ")
	days = 0
	if not bday == "y":
		year -= 1
	days += ((d("%y")+2000) - year) *365
	days += int(days / 4) #to add leap-year days.
	days += int((d("%m") + month) * 30.41)
	days += d("%d") + day
	print("You have been alive for {} days".format(days))


if __name__ == '__main__':
	main()