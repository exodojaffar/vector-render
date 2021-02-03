
class Screen():
	"""docstring for Screen"""
	def __init__(self, HEIGHT, WIDTH, STATE_ZERO = " "):
		
		self.__HEIGHT = HEIGHT
		self.__WIDTH = WIDTH

		self.__STATE_ZERO = STATE_ZERO
		self.__SCREEN = list()

		self.reset_screen()

		pass
		
	def reset_screen(self) -> None:
		for y in range(self.__HEIGHT):	
			line = [self.__STATE_ZERO for x in range(self.__WIDTH)]

			self.__SCREEN.append(line)
			pass

		pass

	def draw_screen(self):
		for linha in self.__SCREEN:
			for pixel in linha:
				print(pixel, end='')

			print()

		pass

	def draw_line(self, start_point: list, end_point: list) -> None:
		X_1, Y_1 = start_point
		X_2, Y_2 = end_point	

		def f(x: float) -> float:
			a = (Y_2 - Y_1)/(X_2 - X_1)
			b = Y_1 - a*X_1

			y = a*x + b

			return y

		step = 1 if X_1 <= X_2 else -1

		for x in range(X_1,X_2+1, step):
			y = round(f(x))

			self.__SCREEN[y][x] = '#'

			pass

		pass

def main():
	# Triangulo
	# POINTS = [[1,1], [5,5],[9,1]]

	# Quadrado
	POINTS = [[1,1], [15,1], [15,15], [1,15]]

	S = Screen(20, 20, '-')

	for i in range(len(POINTS)-1):
		s_point = POINTS[i]
		for point in POINTS[i+1:]:
			S.draw_line(s_point, point)

		pass

	S.draw_screen()
	pass

if __name__ == '__main__':
	main()