#-*- coding: utf-8-*-
if __name__ == '__main__':
	fib = [0, 1]
	count = 0
	fibappend = int()
	while count != 20:
		fibappend = fib[count] + fib[count + 1]
		fib.append(fibappend)
		count += 1
	for num in fib:
		print(num)
