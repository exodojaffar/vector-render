#!/usr/bin/python3

import subprocess as run
run_in_bash = run.run

from time import sleep

"""
A parte de vetores, mapa e transformação pode ser transoformada
em POO, baseado em classe e metodo.
"""

def get_width() -> int:
	inp = len(input("Digite ate o final da tela:\n"))

	if (inp % 2) == 0:
		inp -=1

	return inp

def get_middle(value):
	# Some 1 caso queria o real meio
	# Não some 1 caso queria o meio ja para colocar numa list

	return (value//2) #+ 1

caracteres_sombra = "# @ $ & O 8 [ + - ~".split(' ')
WIDTH = get_width()
HEIGHT = 21

MAPA = [[' ']*WIDTH]*HEIGHT
VERTICES = [[-1,0], [0,1], [1,0]] # Posição dos vertices de um triangulo


def clear_terminal():
	run_in_bash('clear')
	pass

def atualizar_mapa():
	global MAPA, VERTICES

	middle_x = get_middle(WIDTH)
	middle_Y = get_middle(HEIGHT)

	pass

def draw():
	clear_terminal()

	for linha in MAPA:
		for elemento in linha:
			print(f"{elemento}", end="")
		print()

	pass

def main():
	run = True

	while run:
		try:

			atualizar_mapa()
			draw()
			sleep(0.5)
		except KeyboardInterrupt:
			run = False

	pass

if __name__ == '__main__':
	main()