import math

def scale(vectors:list, values:tuple):
	"""
	values-> tuple of 2 positions:
		float, floar
	
	Fist value is the transformation on X
	Second value is the tranformation on Y

	"""
	new_vectors = list()

	for vector in vectors:
		new_vector = [original*transformation for original, transformation in zip(vector, values)]

		new_vectors.append(new_vector)

	return new_vectors

def translate(vectors:list, values: tuple):
	"""
	values -> tuple of 2 positions:
		float, floar
	
	Fist value is the transformation on X
	Second value is the tranformation on Y

	"""
	new_vectors = list()

	for vector in vectors:
		new_vector = [(original+transformation) for original, transformation in zip(vector, values)]

		new_vectors.append(new_vector)

		pass

	return new_vectors

def rotate(vectors:list, deg: float):
	"""
	deg -> graus de rotação
		float
	"""
	pass

def all(transformation_matriz):
	"""
	Essa função ira fazer tudo usando duas matrizes:
		- Original
		- Transformação
	"""
	pass

def test():
	vectors = [[-1,0], [0,1], [1,0]]

	new_vectors_translated = translate(vectors, (2,1))
	print(new_vectors_translated)

	pass

if __name__ == '__main__':
	test()