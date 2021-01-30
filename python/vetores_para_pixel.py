
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

	def draw_line(self, start_point: list, end_point: list) -> None:
		X_1, Y_1 = start_point
		X_2, Y_2 = end_point

		def f(step: float) -> tuple:
			a = (Y_2 - Y_1)/(X_2 - X_1)
			b = Y_1 - a*X_1

			y = a*step + b
			return (step, y)

		pass

def main():
	POINTS = list()

	POINTS.append([[0,0], [5, 5]])

	S = Screen(20, 20)
	S.draw_line([1,8], [2,11])

	pass

if __name__ == '__main__':
	main()