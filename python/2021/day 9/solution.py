import logging
import pprint
import numpy as np
logging.basicConfig(filename="logs.log", filemode='w', level=logging.DEBUG)
logging.disable()

def part1():
	columns = len(open('input.txt', 'r').readline().strip())
	rows = len(open('input.txt', 'r').read().split('\n'))

	matrix = np.array([0]*rows*columns).reshape((rows, columns))

	with open('input.txt', 'r') as f:
		for i in range(rows):
			data = [int(x) for x in f.readline().strip('\n')]
			matrix[i] = data

	low_points = []

	for i in range(rows):
		for j in range(columns):
			num: int = matrix[i][j]
			left, right, top, bottom = [True]*4
			if j>0:
				left = matrix[i][j-1] > num
			if j<(columns-1):
				right = matrix[i][j+1] > num
			if i>0:
				top = matrix[i-1][j] > num
			if i<(rows-1):
				bottom = matrix[i+1][j] > num

			if all([left, right, top, bottom]):
				low_points.append(num)

	risk_level = [(x+1) for x in low_points]
	res = sum(risk_level)
	return res

def part2():
	columns = len(open('input.txt', 'r').readline().strip())
	rows = len(open('input.txt', 'r').read().split('\n'))

	matrix = np.array([0]*rows*columns).reshape((rows, columns))
	points_covered = np.array([False]*rows*columns).reshape(matrix.shape)

	with open('input.txt', 'r') as f:
		for i in range(rows):
			data = [int(x) for x in f.readline().strip('\n')]
			matrix[i] = data

	low_points = []
	low_points_index = []

	for i in range(rows):
		for j in range(columns):
			num: int = matrix[i][j]
			left, right, top, bottom = [True]*4
			if j>0:
				left = matrix[i][j-1] > num
			if j<(columns-1):
				right = matrix[i][j+1] > num
			if i>0:
				top = matrix[i-1][j] > num
			if i<(rows-1):
				bottom = matrix[i+1][j] > num

			if all([left, right, top, bottom]):
				low_points.append(num)
				low_points_index.append((i, j))

	sizes = []
	for ind in low_points_index:
		res = check_9(matrix, ind, points_covered)
		if res > 0:
			sizes.append(res)
	
	sizes.sort()
	
	res = sizes[-1] * sizes[-2] * sizes[-3]
	print(res)

def check_9(matrix, point, points_covered):
	count = 1
	i, j = point
	num = matrix[i][j]
	row, col = matrix.shape

	# return if this point has already been checked
	if points_covered[i][j]:
		return 0

	# return if this point is the boundary point
	if num==9:
		return 0
	
	left = (i,j-1) if j>0 else None
	right = (i,j+1) if (j<(col-1)) else None
	top = (i-1,j) if i>0 else None
	bottom = (i+1,j) if (i<(row-1)) else None
	
	for p in [left, right, top, bottom]:
		if p == None:
			continue
		x,y = p
		k = matrix[x][y]

		# check only if it is greater than the current number
		# to avoid checking the previous point
		if (k > num):
			logging.debug(f"1: Point:{point},num: {num}, count:{count}")
			count += check_9(matrix, p, points_covered)
			
			# mark that it is checked
			points_covered[x][y] = True
			logging.debug(f"2: Point:{point}, count:{count}")
		

	return count	

part2()