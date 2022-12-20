
from rich import print
import sys

def parseInput():
	filename = sys.argv[1];
	with open(filename, 'r') as f:
		return [ int(line.strip()) for line in f.readlines() ]

def shift(inp: list, curr: tuple):
	ind: int = inp.index(curr);
	_, val = inp.pop(ind);
	new_ind: ind = (ind+val)%len(inp);
	inp.insert(new_ind, curr);

def mix(inp: list):
	inp = list(enumerate(inp));
	orig: list = inp.copy();
	n: int = inp[-1][0] + 1;
	for pair in orig:

		curr: int = inp.index(pair);
		shift(inp, pair);

	return inp;

def part1():
	inp: list = list(parseInput());
	n: int = len(inp);

	zero: tuple = (inp.index(0), 0);
	inp = mix(inp);

	zero_ind: int = inp.index(zero);

	x = [1000, 2000, 3000];
	loc = [inp[(zero_ind+y)%n] for y in x ]
	ans: int = sum([p[1] for p in loc])

	print(loc)
	print(ans)

part1();