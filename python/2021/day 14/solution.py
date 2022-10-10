import collections
import pprint

class Polymer:

	pair_insertion = collections.defaultdict(str)

	def __init__(self, polymer):
		self.polymer = polymer

	def steps(self, n):
		count = collections.Counter(self.polymer)
		pairs = [self.polymer[i:i+2] for i in range(len(self.polymer)-1)]
		pair_counts = collections.Counter(pairs)
		for _ in range(n):
			new_count = collections.Counter()
			for pair, n in pair_counts.items():
				p1, p2 = pair
				insert = Polymer.pair_insertion[pair]
				new_count[p1+insert] += n
				new_count[insert+p2] += n
				count[insert] += n
			pair_counts = new_count
		return count	

with open("input.txt", 'r') as f:
	polymer = Polymer(f.readline().strip())
	f.readline()

	for ins in map(str.strip, f.readlines()):
		pair, ch = ins.split(' -> ')
		Polymer.pair_insertion[pair] = ch

new_polymer = polymer.steps(int(input("steps: "))).most_common()
res = new_polymer[0][1] - new_polymer[-1][-1]
print(res)

