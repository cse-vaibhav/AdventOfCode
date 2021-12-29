
import numpy as np

def count_marked(matrix):
	row, col = matrix.shape
	count = 0
	for i in range(row):
		for j in range(col):
			if matrix[i][j] == '#':
				count += 1
	return count

def part1():
	lines = len(open("input.txt", 'r').readlines())
	with open("input.txt", 'r') as f:
		marked = []
		instructions = []

		for i in range(lines):
			inp = f.readline().strip()
			if inp == '':
				break
			marked.append(tuple(map(int, inp.split(','))))
		
		for i in range(len(marked), lines):
			inp = f.readline().strip('\n').split('=')
			if '' in inp:
				break
			fold_along = inp[0][-1]
			x = int(inp[1])
			instructions.append((fold_along, x))

	span = [0,0]
	for x, y in marked:
		if y > span[0]:
			span[0] = y
		if x > span[1]:
			span[1] =  x

	span[0] += 1
	span[1] += 1
	
	matrix = np.array(['.']*span[0]*span[1]).reshape(span)

	for x, y in marked:
		matrix[y][x] = '#'
	for ins in instructions:
		row, col = matrix.shape
		fold_along, x = ins
		if fold_along == 'y':
			new_matrix = np.array(['.']*col*x).reshape((x,col))
			for i in range(row):
				for j in range(col):
					if i < x:
						new_matrix[i][j] = matrix[i][j]
					elif i== x:
						break
					else:
						diff = 2*(i-x)
						if new_matrix[i-diff][j] == '#':
							continue
						new_matrix[i-diff][j] = matrix[i][j]

		if fold_along == 'x':
			new_matrix = np.array(['.']*row*x).reshape((row,x))
			for i in range(row):
				for j in range(col):
					if j < x:
						new_matrix[i][j] = matrix[i][j]
					elif j==x:
						continue
					else:
						diff = 2*(j-x)
						if new_matrix[i][j-diff] == '#':
							continue
						new_matrix[i][j-diff] = matrix[i][j]

		matrix = new_matrix
		break
	return count_marked(matrix)

def part2():
	lines = len(open("input.txt", 'r').readlines())
	with open("input.txt", 'r') as f:
		marked = []
		instructions = []

		for i in range(lines):
			inp = f.readline().strip()
			if inp == '':
				break
			marked.append(tuple(map(int, inp.split(','))))
		
		for i in range(len(marked), lines):
			inp = f.readline().strip('\n').split('=')
			if '' in inp:
				break
			fold_along = inp[0][-1]
			x = int(inp[1])
			instructions.append((fold_along, x))

	span = [0,0]
	for x, y in marked:
		if y > span[0]:
			span[0] = y
		if x > span[1]:
			span[1] =  x

	span[0] += 1
	span[1] += 1
	
	matrix = np.array(['.']*span[0]*span[1]).reshape(span)

	for x, y in marked:
		matrix[y][x] = '#'
	for ins in instructions:
		row, col = matrix.shape
		fold_along, x = ins
		if fold_along == 'y':
			new_matrix = np.array(['.']*col*x).reshape((x,col))
			for i in range(row):
				for j in range(col):
					if i < x:
						new_matrix[i][j] = matrix[i][j]
					elif i== x:
						break
					else:
						diff = 2*(i-x)
						if new_matrix[i-diff][j] == '#':
							continue
						new_matrix[i-diff][j] = matrix[i][j]

		if fold_along == 'x':
			new_matrix = np.array(['.']*row*x).reshape((row,x))
			for i in range(row):
				for j in range(col):
					if j < x:
						new_matrix[i][j] = matrix[i][j]
					elif j==x:
						continue
					else:
						diff = 2*(j-x)
						if new_matrix[i][j-diff] == '#':
							continue
						new_matrix[i][j-diff] = matrix[i][j]
		matrix = new_matrix

	for row in matrix:
		print("".join(row))
part2()


