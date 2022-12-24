
from rich import print
from tqdm import tqdm
import sys

class Part1:

	def parseInput(self):
		with open(sys.argv[1], 'r') as f:
			self.points = [ tuple(map(int, line.strip().split(','))) for line in f.readlines() ];
			print(self.points);

if __name__ == "__main__":

	Part1().parseInput();


