import heapq
from collections import defaultdict
import numpy as np
import pprint

class part1:
	def __init__(self):
		self.n = self.getLines()
		self.matrix = self.getMatrix()
		self.pq = [(0, 0, 0)]
		heapq.heapify(self.pq);

	def getLines(self):
		with open('input.txt', 'r') as f:
			return len(f.readlines());

	def getMatrix(self):
		with open('input.txt', 'r') as f:
			l = [f.readline().strip() for _ in range(self.n)]
			l = np.array([ list(map(int, [ch for ch in line])) for line in l ])
		return l

	def findMinRisk_DP(self, i, j, risk=0):
		if (i >= self.n or j >= self.n):
			return risk;
		risk += self.l[i][j];
		if (i == self.n-1 and j == self.n-1):
			self.dp[i][j] = min([self.dp[i][j], risk]);
			return self.dp[i][j];

		down = self.findMinRisk(i+1, j, risk)
		right = self.findMinRisk(i, j+1, risk)

		self.dp[i][j] = min([down, right, self.dp[i][j]])

		return self.dp[i][j]

	def findMinRisk_PQ(self):
		visited = set()
		cost = defaultdict(int)
		while (len(self.pq) > 0):
			c, row, col = heapq.heappop(self.pq)

			# if already visited
			if (row, col) in visited:
				continue

			# mark it visited
			visited.add( (row, col) )

			cost[(row, col)] = c

			if (row == self.n-1 and col == self.n-1):
				break

			for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
				rr = row + dr;
				cc = col + dc;

				if not (0 <= rr < self.n and 0 <= cc < self.n):
					continue
				
				heapq.heappush(self.pq, (c + self.matrix[rr][cc], rr, cc))

		print(cost[ (self.n-1, self.n-1) ])

	def getMin(self):
		self.findMinRisk(1, 0)
		self.findMinRisk(0, 1)
		return self.dp[self.n-1][self.n-1]

class part2(part1):
	def __init__(self):
		super().__init__()
		self.n *= 5

	def getMatrix(self):
		with open('input.txt', 'r') as f:
			l = [f.readline().strip() for _ in range(self.n)]
			l = np.array([ list(map(int, [ch for ch in line] ))*5 for line in l ]*5)

			for i in range(self.n*5):
				arr = l[i][0:self.n].copy()
				for j in range(self.n, self.n*5, self.n):
					for x in range(self.n):
						if (arr[x] == 9):
							arr[x] = 1;
							l[i][j+x] = arr[x];
						else:
							arr[x] += 1
							l[i][j+x] = arr[x];

			for i in range(self.n, self.n*5):
				arr = l[i - self.n][0:self.n].copy()
				for j in range(0, self.n*5, self.n):
					for x in range(self.n):
						if (arr[x] == 9):
							arr[x] = 1;
							l[i][j+x] = arr[x];
						else:
							arr[x] += 1
							l[i][j+x] = arr[x];
					
		return l

if __name__ == "__main__":
	p2 = part2()
	p2.findMinRisk_PQ()
