from main import clear_terminal, draw

def teste_sombra():

	for x in range(0,HEIGHT):
		for y in range(0, WIDTH):
			value = (x)%10
			print(caracteres_sombra[value], end='')
		print()

	pass

def test():
	MENU = """MENU
0 -> Teste Sombra
1 -> Teste Limpar tela
2 -> Teste Desenha Triangulo
"""
	OPs = [teste_sombra, clear_terminal, draw]

	op = int(input(MENU))

	OPs[op]()

	pass
