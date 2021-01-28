#!/usr/bin/python3

import subprocess as run
run_in_bash = run.run

from time import sleep
from transformations import scale
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

MAPA = list()
for y in range(0, HEIGHT):
	linha = list()
	
	for x in range(0, WIDTH):
		linha.append('-')

	MAPA.append(linha)

	pass


VERTICES = [[-1,0], [3,1], [1,0]] # Posição dos vertices de um triangulo


def clear_terminal():
	run_in_bash('clear')
	pass

def atualizar_vertices():
	global VERTICES

	VERTICES = scale(VERTICES, (2,2))
	pass

def atualizar_mapa():
	global MAPA, VERTICES

	middle_X = get_middle(WIDTH)
	middle_Y = get_middle(HEIGHT)

	for vertice in VERTICES:
		X, Y = vertice 
	
		MAPA[middle_Y - Y][middle_X + X] = caracteres_sombra[0]

	MAPA[middle_Y ][middle_X ] = caracteres_sombra[1]

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

	atualizar_vertices()

	while run:
		# atualizar_vertices()
		atualizar_mapa()
		draw()
		sleep(0.5)
	pass

if __name__ == '__main__':
	main()