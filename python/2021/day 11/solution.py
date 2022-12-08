import numpy as np
import logging
logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG)
logging.disable()

class DumboOctopus:
	octopuses = np.array([]).astype('object')
	justTriggered = []
	population = 0
	flash_count = 0

	def __init__(self, index, energy_level):
		self.ind = index
		self.energy = energy_level
		DumboOctopus.octopuses = np.append(DumboOctopus.octopuses, self)
		DumboOctopus.population += 1

	def take_a_step(self):
		triggered = self.ind in DumboOctopus.justTriggered

		if not triggered:
			if self.energy == 9:
				DumboOctopus.flash_count += 1
				DumboOctopus.justTriggered.append(self.ind)
				for octopus in self.adjacentOctopuses:
					if octopus != None:
						logging.debug(f"\tenergy:{self.energy}, index: {self.ind}")
						octopus.take_a_step()
				self.energy = 0
			else:
				self.energy += 1

	def findAdjacentOctopuses(self):
		i, j = self.ind
		row, col = DumboOctopus.octopuses.shape
		left = j>0
		right = j<(col-1)
		top = i>0
		bottom = i<(row-1)
		leftOctopus = DumboOctopus.octopuses[i][j-1] if left else None
		topOctopus = DumboOctopus.octopuses[i-1][j] if top else None
		bottomOctopus = DumboOctopus.octopuses[i+1][j] if bottom else None
		rightOctopus = DumboOctopus.octopuses[i][j+1] if right else None
		topRightOctopus = DumboOctopus.octopuses[i-1][j+1] if (top and right) else None
		bottomRightOctopus = DumboOctopus.octopuses[i+1][j+1] if (bottom and right) else None
		topLeftOctopus = DumboOctopus.octopuses[i-1][j-1] if (top and left) else None
		bottomLeftOctopus = DumboOctopus.octopuses[i+1][j-1] if (bottom and left) else None
		self.adjacentOctopuses = [leftOctopus,rightOctopus,
									topOctopus, bottomOctopus,
									topRightOctopus, bottomRightOctopus,
									topLeftOctopus, bottomLeftOctopus]

	@classmethod
	def simulate_steps(cls, n:int = 1):
		row, col = cls.octopuses.shape
		for _ in range(n):
			cls.justTriggered.clear()
			for i in range(row):
				for j in range(col):
					cls.octopuses[i][j].take_a_step()

	@classmethod
	def findAllAjacentOctopuses(cls):
		row, col = cls.octopuses.shape
		for i in range(row):
			for j in range(col):
				cls.octopuses[i][j].findAdjacentOctopuses()

	@classmethod
	def getEnergyMap(cls):
		row, col = cls.octopuses.shape
		res = np.zeros(cls.octopuses.shape).astype('int64')
		for i in range(row):
			for j in range(col):
				octopus = cls.octopuses[i][j]
				res[i][j] = octopus.energy
		return res

	@classmethod
	def synchronizingStep(cls):
		step = 0
		res = np.zeros(cls.octopuses.shape).astype('int64')
		while(True):
			cls.simulate_steps(1)
			step+=1
			if ((cls.getEnergyMap() == res).all()):
				break
		return step

def part1(days: int):
	rows = len(open('input.txt', 'r').readlines())
	with open('input.txt', 'r') as f:
		for i in range(rows):
			row = list(map(int, list(f.readline().strip('\n'))))
			cols = len(row)
			for j in range(cols):
				DumboOctopus((i, j), row[j])
	DumboOctopus.octopuses.resize((rows, cols))
	DumboOctopus.findAllAjacentOctopuses()
	DumboOctopus.simulate_steps(days)
	
	return DumboOctopus.flash_count

def part2():
	rows = len(open('input.txt', 'r').readlines())
	with open('input.txt', 'r') as f:
		for i in range(rows):
			row = list(map(int, list(f.readline().strip('\n'))))
			cols = len(row)
			for j in range(cols):
				DumboOctopus((i, j), row[j])
	DumboOctopus.octopuses.resize((rows, cols))
	DumboOctopus.findAllAjacentOctopuses()
	step = DumboOctopus.synchronizingStep()
	return step

if __name__ == "__main__":
	print(f"Part1 : {part1(100)}")
	print(f"Part2 : {part2()}")
