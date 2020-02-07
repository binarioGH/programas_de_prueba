#-*-coding: utf-8-*-

invited = ["Cristina", "Diego", "Danika", "Srishti"]
name = input("What is your name? ")

if not name in invited:
	print("Oof, you were not invited UmU.")

else:
	print("Yaay, here is your invitation.")