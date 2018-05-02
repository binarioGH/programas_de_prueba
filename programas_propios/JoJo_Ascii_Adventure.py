#-*- coding: utf-8 -*-
import random
import subprocess
def game_over(wl):
	subprocess.call(["cmd.exe","/c","cls"])
	repit = input('''
		{}
		
		> Quiere repetir? Y/N: '''.format(wl))
	repit = repit.upper()
	if repit == "Y":
		run()
		
def battle(joestar, choosed_one):
	life = 100
	enemy_life = 100
	while True:
		if life <= 0:
			game_over("P E R D I S T E")
			break
		if enemy_life <= 0:
			game_over("G A N A S T E")
			break

		subprocess.call(["cmd.exe","/c","cls"])
		fight = input('''
			salud de {} [{}]
			salud de DIO [{}]

		          0        0
		        ./!\.    ./!\.
                        ./ \.    ./ \.

			> "a" para atacar y "d" para defender: '''.format(choosed_one, life, enemy_life))
		if fight == "a":
			enemy_life -= random.randint(10, 20)
		elif fight == "d":
			life += random.randint(5, 15)
		enemy_choice = random.randint(0, 1)
		if enemy_choice == 0:
			life -= random.randint(10, 20)
		else:
			enemy_life += random.randint(5, 15)


def run():
	character = True
	# esto lo voy a ocupar despues
	jojos = {"jonathan": [{"zoom punch": 10, "hamon": 15}], "joseph": [{"hamon": 15, "hermit purple": 10}], "jotaro": [{"oraoraora": 20}], "josuke": [{"doradoradora": 20}]}
	while character:
		subprocess.call(["cmd.exe", "/c", "cls"])
		choice = input("escoja un jojo: ")
		choice = choice.lower()
		for jo in jojos:
			if choice == jo:
				character = False
				break
		if choice == "jonathan":
			battle(jojos, choice)
		elif choice == "joseph":
			battle(jojos, choice)
		elif choice == "jotaro":
			battle(jojos, choice)
		elif choice == "josuke":
			battle(jojos, choice)

if __name__ == '__main__':
	run()
	


	