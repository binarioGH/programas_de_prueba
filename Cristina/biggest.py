#-*-coding: utf-8-*-

def get_biggest_number(numbers):
	biggest = numbers[0]
	for number in numbers:
		if number > biggest:
			biggest = number
	return biggest

def main():
	number_list = []
	n = ""
	while n != 0:
		n = int(input("Input a number: "))
		number_list.append(n)
	biggest_number = get_biggest_number(number_list)
	print("The biggest number is {}".format(biggest_number))


if __name__ == '__main__':
	main()

