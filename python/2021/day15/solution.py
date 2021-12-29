import logging
import numpy as np
import collections
import pprint

logging.basicConfig(filename="logs.log", filemode="w", level=logging.DEBUG)
logging.disable()

def precompute(matrix, risk_matrix):
	change = 1
	for i,x in np.ndenumerate(matrix):
		if (i[0] == 0 and i[1] == 0):
			continue
		elif (i[0] == 0):
			risk_matrix[i] = risk_matrix[(0,i[1]-1)] + x
		elif (i[1] == 0):
			risk_matrix[i] = risk_matrix[(i[0]-1,0)] + x
		else:
			risk_matrix[i] = min(risk_matrix[(i[0],i[1]-1)], risk_matrix[(i[0]-1,i[1])]) + x
	
	while (change):
		change = 0
		matrix = np.flip(np.flip(matrix, 0), 1)
		risk_matrix = np.flip(np.flip(risk_matrix, 0), 1)
		risk_matrix, change = optimize(matrix, risk_matrix, change)

		matrix = np.flip(np.flip(matrix, 0), 1)
		risk_matrix = np.flip(np.flip(risk_matrix, 0), 1)
		risk_matrix, change = optimize(matrix, risk_matrix, change)

	return risk_matrix

def optimize(matrix, risk_matrix, change):
	for i, x in np.ndenumerate(matrix):
		if (i[0] == 0 and i[1] == 0):
			continue
		elif (i[0] == 0):
			n = risk_matrix[(0, i[1]-1)] + x
			if risk_matrix[i] > n:
				change += 1
				risk_matrix[i] = n
		elif (i[1] == 0):
			n = risk_matrix[(i[0]-1, 0)] + x
			if risk_matrix[i] > n:
				change += 1
				risk_matrix[i] = n
		else:
			n = min([risk_matrix[(i[0],i[1]-1)], risk_matrix[(i[0]-1,i[1])]]) + x
			if risk_matrix[i] > n:
				change += 1
				risk_matrix[i] = n
	return risk_matrix,change



def part1():
	shape = (100,100)
	matrix = np.zeros(shape).astype('int64')
	risk_matrix = np.full(matrix.shape,99999,dtype=float)
	with open("input.txt", 'r') as f:
		i = 0
		for line in map(str.strip, f.readlines()):
			data = list(map(int, list(line)))
			matrix[i] = np.array(data)
			i += 1
	risk_matrix[(0,0)] = 0
	risk_matrix = precompute(matrix, risk_matrix)
	return risk_matrix.flat[-1]

print(part1())
