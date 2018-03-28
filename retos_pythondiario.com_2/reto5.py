#-*-coding: utf-8-*-
# Construir un pequeño programa que convierta números binarios en enteros. 
if __name__ == '__main__':
	bincode = str(raw_input("introduzca un numero binario: "))
	if len(bincode) == 8:
		for b in bincode:
			if b != "1" and b != "0":
				print("solo unos y ceros.")
				exit()
        
        bincode = bincode[::-1]
        count = 1
        total = 0
        for b in bincode:
        	if b == '1':
        		total += count
        	count += count
        print(total)
    
   