#
# Autor:    diX - Diego Silva
# GitHub:   https://github.com/diwalker
# Email:    dwalkerserver@gmail.com
#
# Apoie meu trabalho: pix telefone 87988370228
from colorama import Fore, init, Back
import time, sys

import acerto2
from main import main1
from acerto2 import main2
from fora import main3
from fora2 import main4

init()

dev = " 	 		                                                                       	    		Developer: diX"
asci = """
 _______      # ________      # ______      # ___   ___     # ______      # _________  #  _______      # ______      # _________  #
/_______/\     #/_______/\     #/_____/\     #/___/\/__/\    #/_____/\     #/________/\ #/_______/\     #/_____/\     #/________/\ #
\::: _  \ \    #\::: _  \ \    #\::::_\/_    #\::.\ \\ \ \   #\::::_\/_    #\__.::.__\/ #\::: _  \ \    #\:::_ \ \    #\__.::.__\/ #
 \::(_)  \/_   # \::(_)  \ \   # \:\/___/\   # \:: \/_) \ \  # \:\/___/\   #   \::\ \   # \::(_)  \/_   # \:\ \ \ \   #   \::\ \   #
  \::  _  \ \  #  \:: __  \ \  #  \_::._\:\  #  \:. __  ( (  #  \::___\/_  #    \::\ \  #  \::  _  \ \  #  \:\ \ \ \  #    \::\ \  #
   \::(_)  \ \ #   \:.\ \  \ \ #    /____\:\ #   \: \ )  \ \ #   \:\____/\ #     \::\ \ #   \::(_)  \ \ #   \:\_\ \ \ #     \::\ \ #
    \_______\/ #    \__\/\__\/ #    \_____\/ #    \__\/\__\/ #    \_____\/ #      \__\/ #    \_______\/ #    \_____\/ #      \__\/ #
##               ##             ##               ##             ##            ##               ##             ##            ##
"""
RESET = "\033[39m"
print(Fore.LIGHTYELLOW_EX + asci)
print(Fore.YELLOW + dev)
print('\033[39m')

print("---------------------------------------------------------------------------------------------------------------")
print(Fore.LIGHTCYAN_EX + "Bem Vindo ao BASKETBOT🏀, o Preditor de Lance Livre no Basquete! Selecione uma opção para analisar ou encerrar.\033[39m")
print("---------------------------------------------------------------------------------------------------------------\n")

def menu():
	print(Fore.LIGHTRED_EX + "1:\033[39m Cesta")
	print(Fore.LIGHTRED_EX + "2:\033[39m Cesta")
	print(Fore.LIGHTRED_EX + "3:\033[39m Pra fora")
	print(Fore.LIGHTRED_EX + "4:\033[39m Pra fora")
	print(Fore.LIGHTRED_EX + "5:\033[39m Para encerrar o programa\n")

	print("-------------------------------")
	option = int(input(Fore.LIGHTCYAN_EX + "Digite o número da sua escolha:\033[39m "))
	print("-------------------------------")

	if option == 1:
			main1()
	elif option == 2:
			main2()
	elif option == 3:
			main3()
	elif option == 4:
			main4()
	elif option == 5:
		print(Fore.LIGHTRED_EX + "O bot está sendo encerrado...\033[39m")
		for i in range(3):
			sys.stdout.flush()
			time.sleep(0.5)
		exit()
	else:
		print(Fore.LIGHTRED_EX + "Opção inválida...\033[39m")
		print("-------------------------------")
		option = int(input(Fore.LIGHTCYAN_EX + "Digite o número da sua escolha:\033[39m "))
		print("-------------------------------")

		if option == "1":
			open(capOne())
		elif option == "2":
			capTwo()
		elif option == 3:
			capThree()
		elif option == 4:
			capFour()
		elif option == 5:
			print(Fore.LIGHTRED_EX + "O bot está sendo encerrado...\033[39m")
			for i in range(3):
				sys.stdout.flush()
				time.sleep(0.5)
			exit()

if __name__ == "__main__":
	menu()

