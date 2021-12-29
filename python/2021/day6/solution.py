import collections
from MyPackage import timeit

@timeit.timeit
def solve(*args):
	with open("input.txt", 'r') as f:
		fishes = list(map(int, f.read().strip().split(',')))

	fish_group = dict()
	for fish in fishes:
		fish_group.setdefault(fish, 0)
		fish_group[fish] += 1

	for _ in range(n):
	
		y = dict()
		y.setdefault(6, 0)
		y.setdefault(8, 0)
		for fish, cnt in fish_group.items():
			y.setdefault(fish-1, 0)
			if fish == 0:
				y[6] += cnt
				y[8] += cnt
			else:
				y[fish - 1] += cnt
		fish_group = y
	print(sum(fish_group.values()))

n = int(input())
solve(n)
