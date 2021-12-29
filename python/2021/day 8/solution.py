import logging
import pprint
from MyPackage import timeit
import collections

logging.basicConfig(filename="logs.log", filemode= 'w', level =logging.DEBUG)
logging.disable()

@timeit.timeit
def part1():

	with open('input.txt', 'r') as f:
		count = 0
		for i in range(200):
			data = f.readline().split(' | ')
			lhs = data[0].split()
			rhs = data[1].split()
			for w in rhs:
				if len(w) in [2, 3, 4, 7]:
					count += 1

	print(count)

@timeit.timeit
def part2():
	with open('input.txt', 'r') as f:
		output = 0
		for i in range(200):
			data = f.readline().strip().split(' | ')
			lhs = data[0].split()
			rhs = data[1].split()
			code = collections.defaultdict(str)
			identified = 0
			for w in lhs:
				length = len(w)
				w = "".join(sorted(w))
				if (length == 2):
					code[1] = w
					identified += 1
					logging.debug("Found 1")
				elif (length == 3):
					code[7] = w
					identified += 1
					logging.debug("Found 7")
				elif (length == 4):
					code[4] = w
					identified += 1
					logging.debug("Found 4")
				elif (length == 7):
					code[8] = w
					identified += 1
					logging.debug("Found 8")

			for w in lhs:
				w = "".join(sorted(w))
				if (len(w) == 6): # either of 0 9 6
					if not all([x in w for x in code[1]]):
						code[6] = w
						identified += 1
						logging.debug("found 6")
						continue
					elif all([x in w for x in code[4]]):
						code[9] = w
						identified += 1
						logging.debug("found 9")
						continue
					elif all([x in w for x in code[1]]):
						code[0] = w
						identified += 1
						logging.debug("found 0")
						continue

			for w in lhs:
				w = "".join(sorted(w))
				if (len(w) == 5): # either 2, 3, 5
					if all([x in w for x in code[1]]):
						code[3] = w
						identified += 1
						logging.debug("found 3")
						continue
					elif all([x in code[9] for x in w]) and code[5]=='':
						code[5] = w
						identified += 1
						logging.debug("found 5")
						continue
					else:
						code[2] = w
						identified += 1
						logging.debug("found 2")
						continue
			ans = ''
			for w in rhs:
				w = "".join(sorted(w))
				for k, v in code.items():
					if (w == v):
						ans += f"{k}"
			output += int(ans)
		print(output)

part2()
