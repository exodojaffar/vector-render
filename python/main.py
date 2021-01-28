#!/usr/bin/python3

import subprocess as run
run_in_bash = run.run

"""
A parte de vetores, mapa e transformação pode ser transoformada
em POO, baseado em classe e metodo.
"""

def get_width() -> int:
	inp = len(input("Digite ate o final da tela:\n"))

	if (inp % 2) == 0:
		inp -=1

	return inp

def get_midle(value):
	# Some 1 caso queria o real meio
	# Não some 1 caso queria o meio ja para colocar numa list

	return (value//2) #+ 1

caracteres_sombra = "# @ $ & O 8 [ + - ~".split(' ')
WIDTH = get_width()
HEIGHT = 21

MAPA = [[' ']*WIDTH]*HEIGHT
VERTICES = [[-1,0], [0,1], [1,0]]

def draw():
	clear_terminal()

	for linha in MAPA:
		for elemento in linha:
			print(f"{elemento}", end="")
		print()

	pass

def clear_terminal():
	run_in_bash('clear')
	pass

def main():
	teste_sombra()

	pass

if __name__ == '__main__':
	main()